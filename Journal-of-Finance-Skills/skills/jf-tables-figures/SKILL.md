---
name: jf-tables-figures
description: Use when finalizing tables and figures for a The Journal of Finance (JF) manuscript. Enforces accessible, self-contained, publication-grade exhibits; it does not decide which results to run.
---

# Tables & Figures (jf-tables-figures)

## When to trigger

- Tables/figures are drafted but notes, units, or formatting are inconsistent
- A reader cannot interpret an exhibit without hunting through the text
- You are aligning main-text exhibits with Internet Appendix exhibits

## JF norm: self-contained, accessible exhibits

JF is general-interest and prizes accessibility. Each exhibit must be **self-contained**: a reader from another subfield should understand it from its caption and notes alone. Because the manuscript faces a **60-page limit** (≥1.5 spacing, 12-pt font), keep only **decisive** exhibits in the body and send the rest to the **Internet Appendix** (bundled at the end of the same PDF, labeled `IA.*`, not counted against 60 pages; see `jf-internet-appendix`).

## Exhibit standards

- **Numbering**: JF uses Roman numerals for tables (Table I, II, …) and Arabic for figures (Figure 1, 2, …); the Internet Appendix mirrors this as `IA.I`, `IA.1`. Keep the schemes consistent.
- **Notes state the inference**: sample, period, units, and the **standard-error/clustering convention** belong in every table note.
- **Economic units**: report magnitudes in interpretable units (bps, % of market cap, Sharpe gain), consistent with JF's general-interest voice.
- **No orphan exhibits**: every table/figure (body or IA) is referenced from the text.

## Checklist

- [ ] Each exhibit interpretable from caption + notes alone
- [ ] Table notes state sample, period, units, and SE/clustering
- [ ] Magnitudes in economic units, not just stars/t-stats
- [ ] JF numbering scheme (Table I…, Figure 1…) and matching `IA.*` in the appendix
- [ ] Only decisive exhibits in the body; rest in the Internet Appendix
- [ ] Body stays within 60 pages

## Anti-patterns

- A table whose meaning is unclear without three paragraphs of text
- Significance stars with no economic magnitude
- Missing SE/clustering convention in the note
- Body crowded with exhibits that belong in the Internet Appendix, breaching the 60-page limit
- Inconsistent numbering between body and appendix

## Output format

```
【All exhibits self-contained?】yes / no
【Notes state SE/clustering + units?】yes / no
【Magnitudes in economic units?】yes / no
【JF numbering consistent (Table I.. / IA.*)?】yes / no
【Decisive-only in body, ≤60 pp?】yes / no
【Next step】jf-writing-style
```
