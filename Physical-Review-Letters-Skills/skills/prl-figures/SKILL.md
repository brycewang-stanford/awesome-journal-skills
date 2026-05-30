---
name: prl-figures
description: Use when designing or auditing figures for a Physical Review Letters manuscript, where a few high-impact figures must carry the central result and count against the length limit. Designs figure strategy; does not run the analysis or write prose.
---

# PRL Figures (prl-figures)

## When to trigger

- You have many candidate figures and need to choose a few
- Your lead figure does not convey the central result at a glance
- Panels are dense, captions are long, or symbols are unreadable at column width
- You are over length and figures (which count against the limit) are a target
- A coauthor wants to "add one more panel just in case"

## Figure strategy for a Letter

A Letter carries **a few high-impact figures only** — typically on the order of three or four, sometimes fewer. Every figure must earn its place against the deductible length limit (figures consume the word budget; see `prl-length-management`). The hierarchy:

- **Lead figure (Fig. 1)** — conveys the central result at a glance. A physicist skimming should grasp the headline from this figure plus its caption alone.
- **Supporting figures** — each makes exactly one additional point (a control, a dependence, a comparison to theory).
- **Everything else** — parameter sweeps, raw traces, extended datasets → Supplemental Material.

If a figure does not advance the single central claim or one essential support, move it to SM.

## Lead-figure design rules

| Principle                     | Practice                                                        |
|-------------------------------|----------------------------------------------------------------|
| One glance, one message       | The eye should land on the central result immediately          |
| Self-explaining               | Headline readable from figure + caption, without the body      |
| Schematic + data              | A small schematic/inset can orient out-of-subfield readers     |
| Theory vs. experiment overlaid| Show the decisive comparison directly, not in separate panels  |
| Annotate the key feature      | Arrow / label on the peak, transition, or scaling that matters |

## Production standards (column format)

- Design for **single-column width** first; use double-column only when the data demand it.
- Fonts, axis labels, and tick numbers must be legible at final printed size (roughly match the body text size).
- Use vector formats (EPS/PDF) for line art; high-resolution raster only for images/maps.
- Curves distinguishable in grayscale and color-blind-safe palettes; do not rely on color alone.
- Define every symbol/line in the caption; keep captions informative but tight (they count against length).
- Match notation in figures to the body; use SI units and consistent significant figures.

## Panel discipline

- Prefer fewer panels with a clear reading order; label (a), (b), (c).
- A six-panel Fig. 1 usually signals that supporting panels belong in SM.
- Insets are powerful for a zoom or a schematic, but must remain legible.

## Checklist

- [ ] Total figure count is small (a few) and each is essential
- [ ] Fig. 1 conveys the central result at a glance
- [ ] Every figure makes exactly one point
- [ ] All figures legible at single-column print size
- [ ] Color-blind-safe; not color-dependent; grayscale-distinguishable
- [ ] Decisive theory/experiment comparison shown directly
- [ ] Captions define all symbols and are as short as clarity allows
- [ ] Non-essential panels/datasets moved to SM

## Anti-patterns

- A lead figure too dense to parse without the body text
- Six-panel megafigures that hide the headline
- Color-only encoding that fails in grayscale or for color-blind readers
- Tiny fonts / unreadable tick labels at column width
- Decorative figures that do not advance the central claim
- Long captions that quietly consume the length budget

## Output format

```
【Figure count】N — each essential?  yes / cut list
【Fig. 1 conveys central result at a glance】yes / redesign
【Per-figure single point】list
【Legibility at column width】pass / fix
【Color-blind / grayscale safe】yes / fix
【Moved to SM】list
【Next】prl-supplementary (SM) or prl-length-management (fit limit)
```

> Figure formatting and length-counting rules are durable in spirit but specific in detail — verify current figure and length-deduction rules on the official APS / PRL author page.
