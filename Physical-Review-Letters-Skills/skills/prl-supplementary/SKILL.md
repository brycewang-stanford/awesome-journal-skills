---
name: prl-supplementary
description: Use when partitioning content between the Physical Review Letters body and its Supplemental Material, ensuring the Letter stands alone while derivations and extended data live in the SM. Organizes the SM; does not write the Letter body.
---

# PRL Supplemental Material (prl-supplementary)

## When to trigger

- The Letter is over length and detail must move out of the body
- A reader cannot follow the Letter without consulting the SM
- You have derivations, extended datasets, or methods detail with no home
- You are unsure what is allowed in SM versus what must stay in the Letter
- Referees of a prior version asked for material that would bloat the body

## The stand-alone rule (non-negotiable)

The Letter must be **fully understandable on its own**. The Supplemental Material *supports* the Letter; it must never be *load-bearing* for the central claim. A reader who never opens the SM should still grasp the result, the evidence for it, and why it matters.

- The central claim, its key evidence, and the decisive control live in the **Letter**.
- The SM holds the exhaustive backup that a skeptical referee or replicator wants.
- Every SM section is **cited from the body** at the point it is relevant.

If removing the SM breaks the argument, the partition is wrong — pull the essential piece back into the Letter (and trim elsewhere via `prl-length-management`).

## What belongs in Supplemental Material

| Content                                            | Home  |
|----------------------------------------------------|-------|
| Full derivations / lengthy algebra                  | SM    |
| Extended datasets, additional samples, full sweeps  | SM    |
| Detailed apparatus, growth, calibration             | SM    |
| Secondary controls and robustness checks            | SM    |
| Full error budget / systematics breakdown           | SM    |
| Numerical convergence studies                        | SM    |
| Additional figures / movies / large tables          | SM    |
| The central claim and its decisive evidence          | Letter|
| The one control ruling out the obvious artifact      | Letter|
| The headline uncertainty                             | Letter|

## SM organization

- Mirror the Letter's logic: order SM sections to match the order they are cited.
- Give SM sections their own clear headings (S1, S2, ...) and self-contained captions.
- SM references: include the works the SM itself needs; follow current APS practice on how SM citations are counted and listed (verify).
- Label SM figures/tables distinctly (Fig. S1, Table S1) to avoid confusion with the Letter.
- Keep the SM honest: it is peer-reviewed alongside the Letter, not a place to hide weak results.

## Checklist

- [ ] The Letter is understandable without ever opening the SM
- [ ] No central-claim evidence is *only* in the SM
- [ ] Every SM section is cited from the body at the relevant point
- [ ] SM sections ordered to match their citation order in the Letter
- [ ] SM figures/tables labeled S1, S2, ... distinctly
- [ ] Derivations, extended data, secondary controls live in SM
- [ ] SM is internally consistent in notation with the Letter
- [ ] SM citation handling follows current APS practice

## Anti-patterns

- A Letter that silently depends on the SM to be understood
- Burying the decisive control or key uncertainty in the SM
- An SM that is a disorganized dump rather than a structured appendix
- SM figures referenced out of order or never cited from the body
- Notation drift between Letter and SM
- Using the SM to smuggle in claims the referees did not vet

## Output format

```
【Letter stands alone】yes / fix (pull back: ...)
【SM sections】S1: ... / S2: ... (cited from body?)
【Central evidence only in SM?】none / move back: ...
【SM figure/table labels】S-prefixed?  yes / fix
【Notation consistent Letter↔SM】yes / fix
【Next】prl-writing-style or prl-length-management
```

> SM scope, citation counting, and file-format rules evolve — verify on the official APS / PRL author page.
