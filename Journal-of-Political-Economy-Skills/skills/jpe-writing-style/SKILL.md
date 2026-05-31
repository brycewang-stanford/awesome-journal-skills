---
name: jpe-writing-style
description: Use when polishing the prose of a Journal of Political Economy (JPE) manuscript into its spare, analytical, economics-first register. Tightens voice, structure, and citation/format house style; it does not fix the economic argument itself (see jpe-theory-model / jpe-identification).
---

# Writing Style & House Conventions (jpe-writing-style)

## When to trigger

- The draft is wordy, hedged, or buries the result under qualifications
- Prose explains procedure before establishing economic purpose
- Citation style, notation, or formatting is inconsistent with JPE conventions
- This is the **late polish** stage — identification and model are already sound

## The JPE voice

JPE prose is **spare, precise, and economics-first**. The writing carries an argument; every paragraph advances the economic case. Sentences are declarative and unhedged where the evidence supports the claim. Jargon is minimized; the economic intuition is stated in words before the algebra. A generalist economist should follow the argument; a specialist should find it rigorous.

Register rules:
- Lead with the economics, then the method. "Higher entry costs reduce competition; we estimate this using..." not "We run a regression of price on entry cost."
- State results plainly. Replace "our findings appear to suggest a potentially meaningful relationship" with "entry costs raise prices by X%."
- Active voice for what the paper does; reserve hedging for genuine uncertainty.
- Define notation once, use it consistently; explain each equation's economic content in prose.
- Cut throat-clearing ("It is important to note that...", "In this paper, we will...").

## Structure conventions

- **Sections**: Introduction → (Model / Theory) → Data / Institutional setting → Empirical strategy → Results → Mechanisms / Robustness → (Counterfactuals) → Conclusion. Order theory before empirics when the model leads.
- **Introduction** does the heavy lifting (see `jpe-literature-positioning`): question, mechanism, gap, what you do, findings.
- **Conclusion** states what economics learned and the portable lesson — not a summary of every table.
- Footnotes for genuine asides, not for results that belong in the text.

## House-style format

- **References: Chicago author-date** (e.g., "(Becker 1968)", "Black and Scholes (1973)"), with an alphabetized reference list — *not* numbered citations. This is a hard University of Chicago Press house convention and a frequent reason a JPE referee flags a mis-templated submission.
- Theory and empirics are integrated within the paper; proofs and heavy robustness go to appendices / online appendix.
- American spelling; consistent decimal and unit conventions; double-spaced manuscript; equations numbered and referenced as "equation (3)."
- Follow the *Chicago Manual of Style* conventions the University of Chicago Press uses. Verify the current author guidelines (including any abstract/length limits) on the journal's official page before submission, as formatting details are updated periodically.

## Checklist

- [ ] Each paragraph advances the economic argument; throat-clearing removed
- [ ] Results stated plainly with magnitudes, hedging reserved for real uncertainty
- [ ] Economics stated before method in every key passage
- [ ] Every equation has a sentence of economic interpretation
- [ ] Citations are Chicago author-date and consistent; reference list complete
- [ ] Notation defined once and used consistently
- [ ] Conclusion states the portable economic lesson, not a table-by-table recap
- [ ] Spelling/format follow Chicago/UChicago Press conventions (verified against current guidelines)

## Anti-patterns

- Hedged, passive prose that obscures a result the evidence actually supports
- Method-first writing that makes the reader hunt for the economics
- Numbered/bracket citations (wrong house style — JPE is Chicago author-date)
- Equations dropped in with no verbal economic interpretation
- A conclusion that recaps every table instead of stating what was learned
- Over-long sentences stacking qualifications; jargon where plain economics would do

## Output format

```
【Voice】economics-first, unhedged where warranted? [y/n + fixes]
【Hedging removed】list of softened claims tightened
【Equations interpreted】all have prose meaning? [y/n]
【Citation style】Chicago author-date verified
【Format】Chicago/UChicago Press conventions checked (verify current guidelines)
【Conclusion】states portable lesson? [y/n]
【Next】jpe-referee-strategy
```
