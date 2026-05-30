---
name: ecta-rebuttal
description: Use when a revise-and-resubmit or referee reports arrive for an Econometrica manuscript and you must write the response letter and plan the revision. Structures the rebuttal and revision; it does not re-derive the theorems (use ecta-theory-model) or rebuild the package (use ecta-replication-package).
---

# Rebuttal and Revision (ecta-rebuttal)

## When to trigger

- A decision letter with a co-editor recommendation and referee reports has arrived
- You need to plan a (typically major) revision and draft a point-by-point response
- A referee flagged a proof gap, a generality limit, or missing finite-sample evidence

Do not draft the response before the revised theorems, simulations, and code are actually
done — promised fixes that are not yet real read as evasive to this referee pool.

## Read the letter correctly

- The **co-editor's letter is the controlling document.** Identify which points the co-editor
  treats as essential vs. which are referee suggestions left to your judgment. Address the
  co-editor's essential points fully and first.
- An R&R at Econometrica is a genuine opportunity but signals **substantial remaining work**
  and likely **another round**. Plan accordingly; do not do the minimum.
- Sort every comment into: (a) genuine error / gap to fix, (b) request for added generality /
  evidence, (c) presentation, (d) a point you will respectfully push back on with argument.

## Response-letter structure

```
Dear Editor / [Co-editor],

We thank you and the referees for [specific, sincere]. The main changes are:
(1) [most important fix — e.g., closed the gap in the proof of Theorem 2],
(2) [added the limiting-distribution / uniform result requested],
(3) [added Monte Carlo design X showing finite-sample size control].
All changes are marked in the revision; new proofs are in Online Appendix §...

— Response to the Co-Editor —
[CE point 1] ... [CE point 2] ...

— Response to Referee 1 —
[R1.1] Comment: "..."
       Response: [what we did, where (section / theorem / appendix), why it resolves the point].
[R1.2] ...

— Response to Referee 2 —
...
```

## Writing each response

- **Quote the comment, then answer.** Make it trivial for the referee to see you addressed it.
- **Point to the exact location** of each change (theorem number, appendix section, table).
- For a **proof gap**: state the corrected argument explicitly; do not just assert it is now fixed.
- For a **generality request**: either deliver the more general result, or argue precisely why the
  current scope is the right one (and add the boundary example that shows the limit binds).
- For **more finite-sample evidence**: add the requested design and report it; show the method's
  behavior even where it is less favorable — selective new evidence is transparent.
- **Disagreement**: allowed, but back it with a precise mathematical argument or a citation, framed
  respectfully. "We respectfully disagree, because [argument]; if the referee still prefers X, we are
  glad to add it."
- **Consistency:** never claim a fix in the letter that the revised manuscript does not contain.

## Revision discipline

- Re-run the **full replication package** after every substantive change; numbers in the letter,
  text, and tables must agree (see `ecta-replication-package`).
- Re-check **theorem numbering and cross-references** after reorganizing — added results shift numbers.
- If a fix changes a result, trace it through: identification → asymptotics → simulations → text.
- Keep a marked-changes version; keep a clean version; keep the response letter in sync with both.

## Checklist

- [ ] Co-editor's essential points identified and addressed first and fully
- [ ] Every referee comment quoted and answered with a location
- [ ] Proof gaps fixed with the corrected argument written out, not merely asserted
- [ ] Generality / evidence requests delivered or precisely rebutted
- [ ] New Monte Carlo / results added where requested; reported fairly
- [ ] Disagreements backed by argument, framed respectfully
- [ ] Full package re-run; letter, text, tables, and code all consistent
- [ ] Theorem numbering and cross-references re-verified after reorganization

## Anti-patterns

- Promising fixes in the letter that the manuscript does not actually contain
- Treating a referee suggestion the co-editor flagged as essential as optional
- "We have addressed this" with no pointer to where
- Patching a proof gap with another hand-wave instead of a complete argument
- Adding only the flattering new simulation and omitting the adverse design the referee implied
- Dismissive disagreement with no mathematical backing
- Forgetting to re-run the package, leaving stale numbers in the revision

## Output format

```
【Co-editor essential points】[...]
【Comment triage】fix: [...] | generality/evidence: [...] | presentation: [...] | push-back: [...]
【Proof gaps closed】[Theorem N: ...]
【New evidence added】[design/result ...]
【Push-backs (with argument)】[...]
【Package re-run + consistent】yes/no
【Status】response letter drafted → re-submit via Editorial Express
```
