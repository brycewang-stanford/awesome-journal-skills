---
name: amr-tables-figures
description: Use when building the conceptual exhibits of an Academy of Management Review (AMR) manuscript — process models, 2x2 typologies, multi-level frameworks, and propositions tables that carry theoretical work. These are CONCEPTUAL figures, NOT data plots; AMR has no charts of results because it has no data.
---

# Conceptual Figures & Propositions Tables (amr-tables-figures)

> AMR exhibits do *theoretical* work. There are no scatterplots, bar charts, or regression
> tables — there is no data. Every figure must be readable directly off the theory: each
> box is a defined construct, each arrow is a stated proposition or mechanism.

## When to trigger

- The theory is built but has no visual model, or the model is decorative
- Your figure is boxes and arrows with no mechanism behind the arrows
- You have many propositions and the reader cannot see their structure
- A typology is asserted in prose but never shown as a grid

## The exhibit toolkit

| Exhibit | Use it when | It must show |
|---------|-------------|--------------|
| Process model | The theory is a sequence / becoming | Stages, triggers, feedback loops, timing — and the engine that drives movement |
| 2x2 (or NxM) typology | The phenomenon has theoretically distinct types | Two theory-derived dimensions; mutually exclusive, jointly exhaustive cells; ideally theorized transitions between cells |
| Multi-level framework | The action spans individual ↔ collective | Levels as horizontal bands; emergence (bottom-up) and top-down arrows labeled |
| Variance/relational model | Core constructs and their specified links | Constructs as nodes; arrows labeled with proposition numbers and form (causal/moderating/mediating) |
| Propositions table | There are many propositions | Pn | statement | underlying mechanism | boundary condition |

## Design rules (what reviewers check)

- **Every box is a defined construct.** No box should appear that was not defined in the text.
- **Every arrow is earned.** Each arrow corresponds to a proposition or a stated mechanism; label it (e.g., "P3") so the figure and text are in lock-step.
- **The mechanism is visible or cited.** A bare arrow with no associated mechanism is decoration. If the space is tight, label the arrow with the proposition number whose mechanism the text supplies.
- **The figure adds, not repeats.** It should let a reader grasp the *structure* of the argument at a glance — not merely re-list the propositions.
- **Levels and time are explicit** when the theory is multi-level or processual.
- **Consistency**: construct labels in the figure match the text exactly; numbering matches.

## Propositions table template

```
| #  | Proposition (constructs + form)                  | Mechanism (why)         | Boundary condition |
|----|--------------------------------------------------|-------------------------|--------------------|
| P1 | The stronger A, the more likely B                | M1: ...                 | holds when C       |
| P2 | A's effect on B is amplified by D                | M2: ...                 | weakens when ...   |
```

## Checklist

- [ ] Every box/node is a construct defined in the text
- [ ] Every arrow maps to a proposition or a stated mechanism, and is labeled
- [ ] The figure shows argument structure, not just a restatement
- [ ] Typologies use theory-derived dimensions; cells are MECE; transitions theorized if relevant
- [ ] Process models show stages, triggers, feedback, timing, and the driving engine
- [ ] Multi-level frameworks label emergence and top-down effects and the levels
- [ ] A propositions table accompanies any paper with more than ~4 propositions
- [ ] Figure labels and numbering match the text exactly
- [ ] Resolution / format meet AOM submission requirements (verify current guidelines)

## Anti-patterns

- A "model" figure of boxes and arrows with no theoretical mechanism behind the arrows
- A figure introducing constructs that never appear in the text
- A typology whose dimensions were chosen for tidiness, not derived from theory
- Arrows with no direction or no form (is it causal? moderating? nobody can tell)
- A figure that simply re-renders the propositions list, adding nothing
- Decorative clip-art / gradients that obscure the logical structure

## Output format

```
【Exhibit type】process / typology / multi-level / relational + propositions table
【Constructs shown】all defined in text? yes/no
【Arrows】each maps to Pn or mechanism? yes/no
【Adds beyond text?】shows structure / merely repeats (fix)
【Format check】meets AOM figure guidelines (verify)
【Next step】amr-writing-style
```
