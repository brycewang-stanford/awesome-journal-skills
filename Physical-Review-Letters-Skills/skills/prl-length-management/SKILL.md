---
name: prl-length-management
description: Use when a Physical Review Letters manuscript exceeds the strict deductible length limit, where figures, equations, and references all count against the budget. Triages what to cut, compress, or move to Supplemental Material; does not rewrite content from scratch.
---

# PRL Length Management (prl-length-management)

## When to trigger

- The manuscript is over the length limit (or you suspect it is)
- You need to know how much "room" a figure or equation actually costs
- You must decide what to cut, compress, or push to Supplemental Material
- A reviewer/editor flagged the Letter as too long
- Late stage: content, figures, and SM are stable and now must fit

## How the PRL length limit works (the deductible model)

A Letter is **short** — on the order of ~3750 words / roughly four journal pages including figures and references; **verify the current limit on the APS author page.** The key feature is that the limit is a **deductible budget**: it is not just running text. Against the same total budget you must count, in current APS practice:

- The body text (the largest term).
- **Figures** — each figure consumes word-equivalents that scale with its printed area / aspect ratio; a large or double-column figure costs more.
- **Equations** — displayed equations consume word-equivalents (roughly per line/equation).
- **References** — the reference list counts against the budget.
- The abstract and table material also count.

APS provides a formula / length guide and an automated length check on submission. The practical consequence: **a beautiful extra figure can cost you a paragraph of text.** Budget figures and text together, not separately.

## Triage order (cut from cheapest loss to most painful)

1. **Move to SM first.** Derivations, extended data, secondary controls, full error budgets → Supplemental Material (see `prl-supplementary`). This is almost always the largest, lowest-pain saving.
2. **Compress figures.** Drop non-essential panels; convert a double-column figure to single-column; merge two figures showing related points. Each reclaims word-equivalents.
3. **Prune equations.** Keep only claim-defining equations inline; move derivation steps to SM; inline short results within a sentence rather than displaying them.
4. **Trim references** to those that establish importance or are needed for trust; consolidate where APS style permits.
5. **Tighten prose** (apply `prl-writing-style`): remove padding, hedging, and figure-transcribing sentences.
6. **Cut scope** as a last resort: demote a supporting claim entirely.

## Cost-awareness table

| Element                         | Budget cost (verify formula)        | Cheapest fix                          |
|---------------------------------|-------------------------------------|---------------------------------------|
| Body paragraph of padding       | high per word                       | delete                                |
| Double-column figure            | large word-equivalent               | shrink to single column / fewer panels|
| Extra figure                    | full figure word-equivalent         | move to SM                            |
| Displayed equation              | per-line word-equivalent            | inline or move derivation to SM       |
| Long reference list             | counts toward limit                 | prune to essential                    |
| Long caption                    | counts as text                      | tighten                               |

## Checklist

- [ ] You have run the current APS length formula / length-check, not just a word count
- [ ] Figures and equations are counted against the budget, not ignored
- [ ] Derivations and extended data are in SM, not the body
- [ ] No double-column figure remains unless the data demand it
- [ ] Only claim-defining equations are displayed inline
- [ ] Reference list is pruned to importance + trust essentials
- [ ] Prose padding/hedging removed (cross-check `prl-writing-style`)
- [ ] The Letter still stands alone after trimming (cross-check `prl-supplementary`)

## Anti-patterns

- Counting only words and being surprised the figures blow the limit
- Trimming load-bearing content (the key control, the headline uncertainty) to fit
- Shrinking fonts in figures to save area (fails legibility instead)
- Padding the SM until the Letter no longer stands alone
- Leaving a decorative double-column figure that costs a paragraph
- Discovering the over-length only at submission, after content is frozen

## Output format

```
【Current length vs. limit】over by ~X (per APS formula, verify)
【Figure/equation/reference budget counted】yes / redo with formula
【Moved to SM】list
【Figures compressed】list (double→single, panels dropped, merged)
【Equations pruned】list
【References pruned】from N to M
【Still stands alone】yes / fix
【Next】prl-cover-letter or prl-submission
```

> The word/page limit, the length formula, and per-element costs are exactly the kind of volatile specifics that change — always verify the current limit and length guide on the official APS / PRL author page.
