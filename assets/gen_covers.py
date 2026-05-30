#!/usr/bin/env python3
"""Generate uniform cover cards for the journal skill packs.

One unified 240x320 card system, rendered to SVG source + 2x PNG. Three card
families share the same template:

  * natural-science depth packs  (Science / Cell / PNAS / NEJM / Lancet)
  * English breadth-bundle flagships (top-5 econ, finance top-3, AOM/SMS,
    FT50 / UTD24 marketing / accounting / operations / IS)
  * the English bundle hero cover

Usage:
  python3 gen_covers.py            # render English flagships + hero (default)
  python3 gen_covers.py --all      # also re-render the natural-science cards

The natural-science cards are committed; they are NOT re-rendered by default so
running this script never churns existing assets. Pass --all to reproduce them.
Uses `rsvg-convert` when available, with macOS `sips` as a fallback.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "covers")
NAVY = "#1f3a5f"

# ---------------------------------------------------------------------------
# Discipline palette (dark enough for white text on the header band + pill)
# ---------------------------------------------------------------------------
PALETTE = {
    "econ":    "#7a1322",  # economics — deep crimson (matches the AER card)
    "finance": "#15406b",  # finance — deep navy-blue
    "mgmt":    "#14635a",  # management / strategy — teal (matches 管理世界)
    "mktg":    "#9a4a06",  # marketing — burnt orange
    "acct":    "#3f3d73",  # accounting — indigo
    "opsis":   "#2f5a34",  # operations & information systems — forest green
    "hero":    "#24304a",  # bundle hero — slate
}

# ---------------------------------------------------------------------------
# Natural-science depth packs (committed; rendered only with --all)
# slug, discipline banner, big name, big font-size, english subtitle, skills, pack dir
# ---------------------------------------------------------------------------
JOURNALS = [
    ("science", "MULTIDISCIPLINARY", "Science",     40, "AAAS",                       12, "Science-Skills"),
    ("cell",    "LIFE SCIENCES",     "Cell",        46, "Cell Press",                 12, "Cell-Skills"),
    ("pnas",    "MULTIDISCIPLINARY", "PNAS",        46, "Nat'l Academy of Sciences",  12, "PNAS-Skills"),
    ("nejm",    "CLINICAL MEDICINE", "NEJM",        44, "New England J. of Medicine", 12, "NEJM-Skills"),
    ("lancet",  "CLINICAL MEDICINE", "The Lancet",  30, "Founded 1823",               12, "Lancet-Skills"),
]

NS_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 320" width="240" height="320">
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

# ---------------------------------------------------------------------------
# English breadth-bundle flagships
# slug, color-key, banner, [name lines (1-2)], big font-size, subtitle (abbr), pill (tier)
# ---------------------------------------------------------------------------
ENGLISH_FLAGSHIPS = [
    # Economics — top-5 (crimson)
    ("american-economic-review",        "econ", "ECONOMICS", ["American", "Economic Review"],   22, "AER · AEJ family", "Top-5"),
    ("quarterly-journal-of-economics",  "econ", "ECONOMICS", ["Quarterly Journal", "of Economics"], 21, "QJE", "Top-5"),
    ("journal-of-political-economy",    "econ", "ECONOMICS", ["Journal of", "Political Economy"], 21, "JPE", "Top-5"),
    ("econometrica",                    "econ", "ECONOMICS", ["Econometrica"],                  27, "ECTA", "Top-5"),
    ("review-of-economic-studies",      "econ", "ECONOMICS", ["Review of", "Economic Studies"], 21, "REStud", "Top-5"),
    # Finance — top-3 (navy)
    ("journal-of-finance",              "finance", "FINANCE", ["Journal of", "Finance"],          24, "JF", "Top-3"),
    ("journal-of-financial-economics",  "finance", "FINANCE", ["Journal of", "Financial Economics"], 19, "JFE", "Top-3"),
    ("review-of-financial-studies",     "finance", "FINANCE", ["Review of", "Financial Studies"], 20, "RFS", "Top-3"),
    # Management / strategy / organization (teal)
    ("academy-of-management-journal",   "mgmt", "MANAGEMENT", ["Academy of", "Management Journal"], 19, "AMJ", "FT50"),
    ("academy-of-management-review",    "mgmt", "MANAGEMENT", ["Academy of", "Management Review"], 19, "AMR", "FT50"),
    ("administrative-science-quarterly","mgmt", "ORGANIZATION", ["Administrative", "Science Quarterly"], 20, "ASQ", "FT50"),
    ("strategic-management-journal",    "mgmt", "STRATEGY", ["Strategic", "Management Journal"], 19, "SMJ", "FT50"),
    # Marketing (burnt orange)
    ("journal-of-marketing",            "mktg", "MARKETING", ["Journal of", "Marketing"],         24, "JM", "FT50"),
    ("journal-of-marketing-research",   "mktg", "MARKETING", ["Journal of", "Marketing Research"], 19, "JMR", "FT50"),
    ("marketing-science",               "mktg", "MARKETING", ["Marketing", "Science"],            26, "Mktg Sci", "FT50"),
    # Accounting (indigo)
    ("the-accounting-review",           "acct", "ACCOUNTING", ["The Accounting", "Review"],        23, "TAR", "FT50"),
    ("journal-of-accounting-research",  "acct", "ACCOUNTING", ["Journal of", "Accounting Research"], 19, "JAR", "FT50"),
    ("journal-of-accounting-and-economics","acct","ACCOUNTING", ["Journal of Acct.", "& Economics"], 21, "JAE", "FT50"),
    # Operations & information systems (forest)
    ("management-science",              "opsis", "OPERATIONS · IS", ["Management", "Science"],     26, "Mgmt Sci", "UTD24"),
    ("operations-research",             "opsis", "OPERATIONS · IS", ["Operations", "Research"],    25, "Oper. Res.", "UTD24"),
    ("mis-quarterly",                   "opsis", "INFORMATION SYSTEMS", ["MIS", "Quarterly"],          28, "MISQ", "UTD24"),
    ("information-systems-research",    "opsis", "INFORMATION SYSTEMS", ["Information", "Systems Research"], 20, "ISR", "UTD24"),
]

# slug, color-key, banner, [name lines], big font-size, subtitle, pill
HERO = ("english-socsci", "hero", "ECON · BUSINESS", ["100"], 62, "flagship English journals", "101 skills")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_card_svg(color, banner, name_lines, bigsize, subtitle, pill):
    """Flexible 240x320 card: 1- or 2-line big name, abbr subtitle, tier pill."""
    w = min(max(len(banner) * 5, 46), 150)
    ux = round(120 - w / 2, 1)
    if len(name_lines) == 1:
        name_svg = (
            f'<text x="120" y="170" text-anchor="middle" '
            f'font-family="Helvetica Neue, Helvetica, Arial, sans-serif" '
            f'font-size="{bigsize}" font-weight="700" fill="#1a1a1a">{esc(name_lines[0])}</text>'
        )
    else:
        name_svg = (
            f'<text x="120" y="146" text-anchor="middle" '
            f'font-family="Helvetica Neue, Helvetica, Arial, sans-serif" '
            f'font-size="{bigsize}" font-weight="700" fill="#1a1a1a">{esc(name_lines[0])}</text>'
            f'<text x="120" y="176" text-anchor="middle" '
            f'font-family="Helvetica Neue, Helvetica, Arial, sans-serif" '
            f'font-size="{bigsize}" font-weight="700" fill="#1a1a1a">{esc(name_lines[1])}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 320" width="240" height="320">
<rect width="240" height="320" fill="#ffffff"/>
<rect x="5" y="5" width="230" height="310" rx="13" fill="#ffffff" stroke="{color}" stroke-width="2"/>
<path d="M5,18 a13,13 0 0 1 13,-13 h204 a13,13 0 0 1 13,13 v60 h-230 z" fill="{color}"/>
<text x="120" y="35" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="10.5" letter-spacing="2.5" font-weight="700" fill="#ffffff">{esc(banner)}</text>
<rect x="{ux}" y="45" width="{w}" height="2" rx="1" fill="#ffffff" opacity="0.7"/>
<text x="120" y="63" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="8.5" letter-spacing="1.5" fill="#ffffff" opacity="0.8">JOURNAL · AGENT SKILLS</text>
{name_svg}
<text x="120" y="238" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="11" fill="#6a6a6a">{esc(subtitle)}</text>
<line x1="42" y1="276" x2="198" y2="276" stroke="{color}" stroke-width="1" opacity="0.3"/>
<rect x="78" y="285" width="84" height="22" rx="11" fill="{color}"/>
<text x="120" y="300" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="11" font-weight="700" fill="#ffffff">{esc(pill)}</text>
</svg>
'''


def render_png(svg_path, png_path):
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "480", "-h", "640", "-o", png_path, svg_path], check=True)
        return
    if shutil.which("sips"):
        subprocess.run(["sips", "-s", "format", "png", "-z", "640", "480", svg_path, "--out", png_path],
                       check=True, stdout=subprocess.DEVNULL)
        return
    raise SystemExit("Install rsvg-convert (librsvg) or run this script on macOS with sips.")


def write_card(slug, svg, also_paths=None):
    os.makedirs(COVERS, exist_ok=True)
    svg_path = os.path.join(COVERS, f"{slug}.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    render_png(svg_path, os.path.join(COVERS, f"{slug}.png"))
    for p in (also_paths or []):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        render_png(svg_path, p)
    return svg_path


def render_natural_science():
    for slug, banner, bigname, bigsize, subtitle, skills, packdir in JOURNALS:
        svg = NS_SVG.format(navy=NAVY, banner=esc(banner), bigsize=bigsize,
                            bigname=esc(bigname), subtitle=esc(subtitle), skills=skills)
        pack_cover = os.path.join(ROOT, packdir, "assets", "cover.png")
        write_card(slug, svg, also_paths=[pack_cover])
        print(f"  {slug}: wall png + {packdir}/assets/cover.png")


def render_english_flagships():
    for slug, ckey, banner, lines, bigsize, subtitle, pill in ENGLISH_FLAGSHIPS:
        svg = build_card_svg(PALETTE[ckey], banner, lines, bigsize, subtitle, pill)
        write_card(slug, svg)
        print(f"  {slug}: {pill} ({subtitle})")


def render_hero():
    slug, ckey, banner, lines, bigsize, subtitle, pill = HERO
    svg = build_card_svg(PALETTE[ckey], banner, lines, bigsize, subtitle, pill)
    bundle_cover = os.path.join(ROOT, "English-SocialScience-Journal-Skills", "assets", "cover.png")
    write_card(slug, svg, also_paths=[bundle_cover])
    print(f"  hero {slug}: wall png + English-SocialScience-Journal-Skills/assets/cover.png")


if __name__ == "__main__":
    print("English flagship cards:")
    render_english_flagships()
    print("Hero:")
    render_hero()
    if "--all" in sys.argv:
        print("Natural-science cards (--all):")
        render_natural_science()
    print("done")
