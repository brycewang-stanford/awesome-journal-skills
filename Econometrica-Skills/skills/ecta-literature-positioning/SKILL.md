---
name: ecta-literature-positioning
description: Use when locating an Econometrica result precisely within the methods / theory lineage it extends, and when writing the related-work paragraphs that pre-empt "how does this differ from X?" Builds the positioning — it does not judge overall fit (use ecta-topic-selection) or state the theorem (use ecta-theory-model).
---

# Literature Positioning (ecta-literature-positioning)

## When to trigger

- The related-work section lists papers but never says how *this* result differs formally
- You suspect a referee will name a classic theorem/estimator your result must beat or nest
- Reviewers might think the contribution is already implied by a known result
- The lineage of assumptions (who introduced each, who relaxed it) is unclear

## The positioning bar at Econometrica

Econometrica referees are typically the people who wrote the results you are extending.
Positioning is not a literature dump — it is a **precise statement of the formal
relationship** between your result and the closest prior results. For each key neighbor,
say exactly one of: *we nest it*, *we generalize it*, *we weaken its assumption*, *we
provide what it lacked* (e.g., the limiting distribution, uniqueness, a constructive proof).

## Map the lineage

Build a small map before writing prose:

1. **Foundational result** — the classic theorem/estimator the literature builds on
   (e.g., the GMM framework, the relevant fixed-point / representation theorem, the
   baseline limit theorem). Cite it precisely.
2. **Direct antecedents** — the 3–6 papers your result most directly competes with or
   extends. For each, record: their setting, their key assumption, their conclusion.
3. **Your delta** — for each antecedent, the single formal sentence describing the
   difference (weaker assumption / broader class / sharper rate / added uniqueness /
   added asymptotics / constructive vs. existential).

## Positioning paragraph template

```
The closest result is [Author, Year], who [conclusion] under [assumption A]. We obtain
[our conclusion] under [weaker assumption A′], which [permits case / yields object] not
covered there. [Author2, Year] consider [related setting] but [lack object / impose
restriction]; our [theorem N] supplies [that object]. Unlike [strand], we do not require
[restrictive condition], at the cost of [honest cost].
```

State costs honestly: a referee who finds an unacknowledged cost reads the rest of the
paper suspiciously.

## What to get right

- **Attribution of assumptions.** Name who introduced each assumption you use and who
  first relaxed it. Mis-attribution is a credibility hit with this referee pool.
- **Nesting claims.** If you claim your result nests a known one, show the special case
  explicitly (often a one-line corollary or remark). Unsupported "nests" claims invite a
  counterexample.
- **Independent / contemporaneous work.** Acknowledge concurrent results fairly; do not
  overclaim priority.
- **The right objects.** For theory, cite the precise theorem (with number) you rely on,
  not just the paper.

## Checklist

- [ ] Foundational result cited precisely (theorem-level, not just paper-level)
- [ ] 3–6 direct antecedents, each with a one-sentence formal delta
- [ ] Every "we generalize / nest" claim backed by an explicit special case
- [ ] Assumptions attributed to their originators correctly
- [ ] Honest statement of what your result costs relative to the closest prior result
- [ ] Contemporaneous / independent work acknowledged
- [ ] No padding: every cited paper bears on the contribution's boundary

## Anti-patterns

- A related-work paragraph that lists ten papers but never states a formal difference
- Claiming to "generalize" a result while quietly imposing a *stronger* assumption elsewhere
- Ignoring the obvious classic theorem a referee will immediately compare you to
- Citing a survey instead of the original theorem your proof depends on
- Overclaiming priority over contemporaneous working papers

## Output format

```
【Foundational result】...
【Direct antecedents】[A (assumption→conclusion), B, ...]
【Deltas】[vs A: weaken X; vs B: add limiting distribution; ...]
【Nesting shown?】yes (corollary N) / no — needs explicit special case
【Honest cost】...
【Next step】ecta-identification
```
