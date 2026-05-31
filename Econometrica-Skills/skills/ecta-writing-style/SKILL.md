---
name: ecta-writing-style
description: Use as a late-stage polish for an Econometrica manuscript to enforce the terse, formal, theorem-numbered house style and clean mathematical exposition. Polishes prose and notation; it does not fix the proof (use ecta-theory-model) or the simulations (use ecta-robustness).
---

# Writing Style (ecta-writing-style)

## When to trigger

- The introduction spends pages on motivation before stating any result
- Assumptions and definitions are buried in prose instead of numbered and set off
- Notation is inconsistent, overloaded, or introduced after first use
- The draft reads like an applied paper (long narrative) rather than a formal one

Trigger this **late**, after the theorems and simulations are stable. Do not polish prose
over an unstable proof.

## The Econometrica register

Econometrica prose is **terse, precise, and formal**. The reader is a specialist. Value is
signaled by the result and its proof, not by rhetorical motivation. The journal's house
style is theorem-numbered LaTeX (the de facto standard is `amsthm`/`amsmath`), and the
**45-page** main-text limit (incl. references and appendices; font ≥12pt, line spacing ≥1.5,
margins ≥1.25in) actively rewards economy — verbose motivation costs pages you need for the
proof architecture. This is a sharper formal register than the narrative style that suits
AER / QJE / JPE / REStud. Concretely:

1. **State the result early.** The introduction should reach the contribution — ideally an
   informal statement of the main theorem — quickly, then explain why it is hard and how the
   proof works. Avoid a long throat-clearing literature tour up front.
2. **Definitions and assumptions are displayed, numbered objects**, not asides in a sentence.
   A reader should be able to find Assumption 2 instantly.
3. **Every symbol is defined before use**, used consistently, and not reused for two things.
   Keep a private notation table to enforce this.
4. **Say what is proven and what is assumed.** Distinguish clearly between an assumption, a
   claim proven in the paper, and a claim cited from elsewhere.
5. **Economy.** Cut sentences that restate the math in words without adding interpretation.
   But *do* give the one sentence of economic / inferential interpretation each key result deserves.

## Mathematical exposition

- **Theorem environments** (Definition / Assumption / Lemma / Proposition / Theorem /
  Corollary) numbered consistently; cross-reference by number.
- **Proof sketches** in the body, full proofs in the **Supplemental Material** when long (the
  body's 45 pages are scarce) — but the body must convey the architecture and the hard step.
- **Display long equations**; number only those referenced later.
- **Interpretation paragraphs.** After a theorem, one short paragraph: what it means, what is
  surprising, what assumption is doing the work. This is where the economics lives.

## Structure of a methods/theory paper

A common, referee-friendly skeleton:
1. Introduction (problem, informal main result, relation to closest prior work, roadmap)
2. Model / setup and assumptions (numbered)
3. Main results (theorems, with proof sketches)
4. Monte Carlo / numerical illustration
5. (If applicable) empirical application
6. Conclusion (brief)
7. Appendix / Supplemental Material (full proofs, additional results, Monte Carlo detail)

## Checklist

- [ ] Contribution / informal main theorem stated within the first ~2 pages
- [ ] Definitions and assumptions are numbered, displayed objects
- [ ] Every symbol defined before use; no symbol overloaded
- [ ] Assumed vs. proven vs. cited is unambiguous throughout
- [ ] Each main result followed by one short interpretation paragraph
- [ ] Theorem numbering consistent; cross-references by number, not "above/below"
- [ ] Full proofs in the Supplemental Material; body conveys architecture + hard step
- [ ] Body fits the 45-page limit (incl. references and appendices); secondary material moved to Supplemental Material
- [ ] Prose trimmed of restating-the-math-in-words filler

## Anti-patterns

- Three pages of motivation before the first formal statement
- Assumptions stated inline in a paragraph so a referee cannot find them
- The same letter used for a parameter and an index in different sections
- "It is well known that ..." doing the work of a citation or a proof
- Verbose narrative that mimics an applied paper's storytelling
- A theorem with no interpretation paragraph — the reader is left to guess the point
- Cross-references like "the theorem above" that break when the paper is reorganized

## Output format

```
【Result stated early?】yes / no — currently first appears p...
【Assumptions numbered/displayed?】yes/no
【Notation conflicts】[...]
【Interpretation paragraphs present?】yes/no — missing after: [...]
【Register】formal-terse / too narrative — fixes: [...]
【Next step】ecta-replication-package
```
