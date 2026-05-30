---
name: pnas-figures
description: Use to finalize PNAS display items — column-width sizing (~9 / 11.4 / 18 cm), minimum font sizes, show-the-data with n and defined error bars, scale bars, colorblind-safe palettes, legend structure, image integrity, and color-mode notes. Enforces figure rigor before submission.
---

# Display Items (pnas-figures)

## When to trigger

- Figures and tables push the page/item allowance (`pnas-writing`).
- Fonts are unreadable at print size, or colors are not colorblind-safe.
- Bar charts hide the underlying data (no points, no n).
- Panels are screenshots of software output pasted into the figure.
- You are unsure which column width to design to.

## Sizing for PNAS columns

PNAS is a multi-column journal; design each figure to render at a standard print width **without rescaling text**:

- **1 column** ≈ **9 cm** wide
- **1.5 column** ≈ **11.4 cm** wide
- **2 columns (full width)** ≈ **18 cm** wide

> Confirm exact widths in current PNAS author/digital-art guidelines.

- Minimum font in the final figure: **~6–8 pt** (sans-serif, e.g., Helvetica/Arial), legible after reduction to print size.
- Line weights ≥ ~0.5 pt; avoid hairlines that vanish in print.
- Submit at the required resolution (line art high-dpi; halftones/photos at the specified dpi) — confirm specs.

## Show the data, not just the summary

- Replace bar-of-means with **dot plots / box+points / violins+points** wherever n is small.
- Always state **n** in the legend, and **what n is** (cells? animals? subjects? independent experiments?).
- Error bars must be **defined** in the legend (SD vs SEM vs 95% CI) — never undefined.
- For images (blots, micrographs): include **scale bars**, and keep full, uncropped key blots for SI Appendix.

## Color and accessibility

- Use a **colorblind-safe palette** (avoid red/green as the only contrast).
- Don't encode meaning by color alone — add shape/pattern/labels.
- **Color mode:** prepare figures in **RGB** for online; PNAS prints in color and may request or convert to **CMYK** for print — confirm the current color-figure policy and any charges. Check that figures remain interpretable in grayscale.
- No rainbow/jet colormaps for continuous data — use perceptually uniform maps (viridis, etc.).

## Figure legend structure

Each legend: a short **title sentence** (the claim of the figure), then per-panel descriptions (A, B, C…), then statistics (test, n, error-bar definition, exact P or values). The legend should let the figure stand alone.

## Integrity rules (non-negotiable)

- No selective deletion, splicing, or beautification of gels/blots/images without a labeled boundary; disclose any grouping.
- Quantitative comparisons must come from the **same** experiment/exposure.
- Keep unprocessed source images and source data — PNAS may request them (`pnas-data`).

## Multi-panel discipline

- Keep panels purposeful; if a figure sprawls, split it or move panels to SI Appendix.
- Consistent axis scales across comparable panels.
- One message per figure; the legend title states it.

## Output format

```
【Item count】 figures + tables vs page/item allowance (confirm guidelines) → ok / over
【Sizing】 designed at 9 / 11.4 / 18 cm? fonts ≥ ~6–8 pt? yes/no
【Data shown】 points + n + defined error bars? yes/no
【Color】 colorblind-safe? RGB online / CMYK-print aware? grayscale-readable? yes/no
【Integrity】 scale bars / uncropped blots in SI / source data kept? yes/no
【Fixes】 [...]
【Next】 pnas-statistics
```

## Anti-patterns

- **Do not** paste raw Stata/Prism/ImageJ screenshots as figures.
- **Do not** use bars to hide n=3 with huge spread — show the points.
- **Do not** leave error bars undefined or mix SD and SEM across panels.
- **Do not** rely on red-vs-green as the sole encoding.
- **Do not** assume color print is free — confirm the color policy.
