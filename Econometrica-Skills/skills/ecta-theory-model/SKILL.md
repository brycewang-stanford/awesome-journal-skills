---
name: ecta-theory-model
description: Use when the central theorem of an Econometrica manuscript must be stated cleanly and proven completely — assumptions, generality, and proof strategy. Builds and audits the theorem-and-proof core; it does not derive the identification/asymptotic conditions (use ecta-identification) or run simulations (use ecta-robustness).
---

# Theorem and Proof Strategy (ecta-theory-model)

## When to trigger

- The central result is stated informally or its conditions are scattered through the text
- The proof has gaps: "it is easy to see," "by a standard argument," or a missing step
- Regularity conditions are invoked mid-proof but never stated as assumptions
- You are unsure whether the result is as general as claimed, or whether the proof secretly uses more

This is the heart of an Econometrica paper. The product is a **complete, correct proof** of a
**general, cleanly stated** theorem.

## Structure: definitions → assumptions → theorems → proofs

Organize the formal content in this order, with consistent theorem numbering:

1. **Definitions** — every object used in the theorem (spaces, operators, parameter set,
   solution concept) defined before it appears.
2. **Assumptions** — numbered, each stated once, each used. Group standing assumptions
   separately from those invoked only for specific results.
3. **Theorems / Propositions / Lemmas** — the headline result first or clearly flagged;
   supporting lemmas factored out so the main proof reads cleanly.
4. **Proofs** — in-text for short proofs; the **full proof in the Supplementary / Online
   Appendix** when length would break the exposition. Either way the proof must be complete.

## Stating the theorem

- State the theorem so it is **self-contained**: a reader should be able to verify the
  hypotheses and conclusion without hunting through the text.
- Reference assumptions by number in the hypothesis ("Under Assumptions 1–3, ...").
- Make the conclusion a precise mathematical statement (existence, the limiting law, the
  representation, the bound), not a verbal summary.
- If the result is sharp (assumptions are necessary, the rate is optimal), say so and prove it
  or cite the matching lower bound.

## Proof strategy toolkit

Pick the architecture before writing line-by-line:

| Result type | Typical machinery |
|-------------|-------------------|
| Existence of equilibrium / solution | Fixed-point (Brouwer / Kakutani / Banach / Schauder), Berge maximum theorem |
| Representation theorem | Separation / Hahn–Banach, mixture-space, biseparable arguments |
| Consistency | Uniform law of large numbers, argmax / M-estimation continuity, identification + compactness |
| Limiting distribution | CLT (for arrays / dependent data), delta method, empirical-process / Donsker arguments, stochastic equicontinuity |
| Uniqueness / comparative statics | Contraction, monotone-comparative-statics (lattice / single-crossing), index theory |
| Bounds / minimax | Le Cam two-point / Fano, coupling |

Write the **proof sketch first** (the architecture and the one or two hard steps), then expand
every step. Flag the genuinely novel step — referees want to see where the work is.

## Generality audit

- For each assumption: is it **used**? Locate the line of the proof that needs it. Unused
  assumptions must go.
- Is each assumption **as weak as the proof allows**? If the proof only needs continuity, do
  not assume differentiability.
- Does the result hold on the **largest natural class**, or is it tied to a parametric example?
  If the latter, either generalize or reframe honestly as an example.
- Are there **edge cases** (boundary of the parameter space, degenerate distributions, ties,
  non-uniqueness) the statement quietly excludes? State the exclusions.

## Checklist

- [ ] Every object in the theorem is defined before use
- [ ] Assumptions numbered; each is used at an identifiable step; none redundant
- [ ] Theorem statement is self-contained and precisely mathematical
- [ ] Proof complete — no "easy to see," no skipped step; full version in Online Appendix if long
- [ ] The novel / hard step is flagged and given full detail
- [ ] Regularity conditions invoked in the proof all appear as stated assumptions
- [ ] Generality audited: assumptions minimal; result not secretly an example
- [ ] Sharpness addressed (necessity / optimal rate) where claimed

## Anti-patterns

- "It is easy to see that ..." standing in for the load-bearing step
- "By standard arguments" where the argument is not standard in this setting
- A regularity condition that appears only inside the proof, never in the assumptions
- Differentiability / compactness assumed for convenience but never genuinely needed
- A theorem that holds only for one functional form, presented as general
- Existence proven, uniqueness silently assumed
- Citing a CLT / fixed-point theorem whose hypotheses your setting does not actually satisfy

## Output format

```
【Central theorem】... (one-line statement + assumption numbers)
【Proof architecture】fixed-point / ULLN+M-estimation / empirical process / ...
【Hard step】...
【Assumptions audit】all used? [yes/no — list unused]; minimal? [...]
【Generality】largest class: ...; excluded edge cases: ...
【Full proof location】in-text / Online Appendix §...
【Next step】ecta-robustness
```
