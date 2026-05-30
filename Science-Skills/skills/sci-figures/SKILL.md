---
name: sci-figures
description: Use to finalize Science display items — panel/word budget, column-width sizing, minimum font sizes, color-accessibility, and showing the data (points over bars). Enforces figure rigor before submission.
---

# Display Items (sci-figures)

## When to trigger

- Figure count exceeds the format budget (Report ≤4, Article ≤6).
- Fonts are unreadable at print size, or colors are not colorblind-safe.
- Bar charts hide the underlying data (no points, no n).
- Panels are screenshots of software output pasted into the figure.

## Sizing for Science columns

Design figures to render at final print width without rescaling text:

- **1 column** ≈ 5.5 cm wide
- **2 columns** ≈ 12 cm wide
- **Full page** ≈ 18 cm wide
- Minimum font in the final figure: **~6 pt** (sans-serif, e.g., Helvetica/Arial). Text must stay legible after reduction.
- Line weights ≥ 0.5 pt; avoid hairlines that vanish in print.

## Show the data, not just the summary

- Replace bar-of-means with **dot plots / box+points / violins+points** wherever n is small.
- Always state **n** (and what n is: cells? animals? independent experiments?) in the legend.
- Error bars must be **defined** in the legend (SD vs SEM vs 95% CI) — never undefined.
- For images (blots, micrographs): show **scale bars**, and present full, uncropped key blots in Supplementary.

## Color and accessibility

- Use a **colorblind-safe palette** (avoid red/green as the only contrast).
- Don't encode meaning by color alone — add shape/pattern/labels.
- RGB color mode for online; ensure adequate contrast in grayscale.
- No rainbow/jet colormaps for continuous data — use perceptually uniform maps (viridis, etc.).

## Figure legend structure

Each legend: a short **title sentence** (the claim of the figure), then per-panel descriptions (A, B, C…), then statistics (test, n, error-bar definition, P values or exact values). The legend should let the figure stand alone.

## Integrity rules (non-negotiable)

- No selective deletion, splicing, or beautification of gels/blots/images without a labeled boundary; disclose any grouping.
- Quantitative comparisons must come from the **same** experiment/exposure.
- Keep unprocessed source images and source data — Science may request them (`sci-data`).

## Multi-panel discipline

- ≤ ~6 panels per figure; if more, split or move to Supplementary.
- Consistent axis scales across comparable panels.
- One message per figure; the legend title states it.

## Output format

```
【Item count】 N (budget: Report ≤4 / Article ≤6) → ok / over
【Sizing】 designed at 5.5 / 12 / 18 cm? fonts ≥6 pt? yes/no
【Data shown】 points + n + defined error bars? yes/no
【Colorblind-safe】 yes/no (palette used)
【Integrity】 scale bars / uncropped blots in SM / source data kept? yes/no
【Fixes】 [...]
【Next】 sci-statistics
```

## Anti-patterns

- **Do not** paste raw Stata/Prism/ImageJ screenshots as figures.
- **Do not** use bars to hide n=3 with huge spread — show the points.
- **Do not** leave error bars undefined or mix SD and SEM across panels.
- **Do not** rely on red-vs-green as the sole encoding.
