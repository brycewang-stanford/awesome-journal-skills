---
name: restud-literature-positioning
description: Use when positioning a The Review of Economic Studies (REStud) manuscript against the closest related work — confronting the nearest papers and stating the marginal contribution precisely. Sharpens positioning; does not write the full introduction or run empirics.
---

# REStud Literature Positioning (restud-literature-positioning)

## When to trigger

- The related-work discussion is a list of citations rather than an argument
- The user cannot name the single closest paper and what theirs adds
- A referee or seminar comment was "how is this different from [X]?"
- The contribution is original (per `restud-topic-selection`) but its *location* in the literature is unclear

## What REStud positioning must do

REStud is general-interest and weights theory and applied work equally, so the positioning has two jobs at once:

1. **Confront the closest papers honestly.** Name the 3–5 nearest results and state precisely what each one already established and what it could not.
2. **Make the marginal contribution legible to a non-specialist on either side.** Because the handling editor and referees may sit on the theory *or* the applied side (the Joint Managing Editors span IO/applied econometrics, micro theory, and information economics), an applied paper should be legible to a theorist and a theory paper to an applied reader. Models that defined whole literatures appeared here first — Mirrlees (1971) on optimal taxation, Stiglitz (1974) on sharecropping incentives — so the register is "this changes how the field models X," not "this adds new data to X."

A REStud-quality positioning paragraph is an *argument*, not a literature dump: "Paper A established X but assumed Y; paper B relaxed Y but only for setting Z; we do W, which neither could, because [our model / design / data]."

## Building the positioning

### Step 1 — The nearest-neighbor map

List the closest papers in two rings:

- **Inner ring (3–5):** papers a referee will say you must beat or extend. For each: what it shows, its key assumption or limitation, and the one sentence distinguishing yours.
- **Outer ring:** the broader literatures the result speaks to (this is where general interest is demonstrated). Two to three strands, each with a canonical anchor citation.

### Step 2 — The "why now / why not before" clause

State why the contribution was not made earlier: a method that did not exist, data that was not available, a model that was not tractable, or a fact no one had documented. This is the spine of an original-contribution claim.

### Step 3 — Confront, do not bury

Cite the closest competitor in the introduction, in the main text, not in a footnote. Referees who suspect you are hiding the nearest paper turn hostile.

### Step 4 — Canonical anchors

REStud referees expect the foundational theory or methods references to be present (e.g., the seminal model your framework extends, or the identification-method papers your design relies on). Missing the obvious canonical citation reads as not knowing the field.

## Checklist

- [ ] Inner-ring papers (3–5) named, each with "what it could not do"
- [ ] One-sentence distinguisher for each inner-ring paper
- [ ] Outer-ring strands identified (demonstrating general interest)
- [ ] "Why now / why not before" clause written
- [ ] Closest competitor cited in the introduction, not a footnote
- [ ] Canonical theory / method anchors present
- [ ] Positioning is an argument, not a list

## Anti-patterns

- A "related literature" paragraph that is a string of "(Author, Year; Author, Year)" with no argument
- Hiding the single closest paper to inflate apparent novelty — referees find it and it costs credibility
- Over-claiming ("the first paper to ...") when an honest reader can name a precedent
- Positioning only within the narrow subfield, so the general-interest claim is unsupported
- Citing your own working papers as the main precedent while ignoring the field's anchor results

## Output format

```
【MARGINAL CONTRIBUTION】<one sentence, relative to the literature>
【INNER RING】[paper — what it could not do — your distinguisher] x3-5
【OUTER RING STRANDS】<2-3 literatures + anchor cites>
【WHY-NOT-BEFORE CLAUSE】<one sentence>
【CANONICAL ANCHORS PRESENT】yes / missing: [...]
【NEXT SKILL】restud-identification (empirical) | restud-theory-model (theory)
```
