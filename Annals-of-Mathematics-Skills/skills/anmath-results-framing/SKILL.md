---
name: anmath-results-framing
description: Use when stating the main theorem(s) of a pure-mathematics manuscript precisely, establishing their significance, and positioning them against prior work for an Annals of Mathematics submission. Crafts statements and positioning; does not write the proof (see anmath-methods).
---

# Stating the Main Theorem(s) (anmath-results-framing)

## When to trigger

- Your main result is described in a paragraph but not stated as a precise theorem
- The introduction does not make the significance unmistakable in the first page
- Readers cannot tell which statement is the headline and which are corollaries
- You have not located your theorem relative to the prior state of the art

## How to state the main theorem

A reader should be able to find the precise main theorem on or near the first page and
understand exactly what is claimed without reading the proof.

1. **State it precisely and self-containedly.** Every hypothesis explicit; every object
   defined or referenced. No "under suitable conditions" hand-waving.
2. **Quantify the advance.** Make clear what is new: which hypothesis is removed, which
   bound is sharpened, which case is now covered, which conjecture is settled.
3. **Separate headline from consequences.** One (or few) Main Theorem(s); corollaries and
   special cases stated separately so the contribution is unambiguous.
4. **Give the sharpest true statement.** Do not under-claim out of caution or over-claim
   beyond what the proof delivers; the statement and the proof must match exactly.

## Introduction architecture (Annals style)

| Element | Purpose |
|---------|---------|
| Problem and history | Why this question matters and what was known |
| Precise statement of Main Theorem | The headline, fully rigorous, early |
| What is new vs. prior work | Named comparison to the closest prior results |
| Consequences / corollaries | Why the result has reach |
| Method in one paragraph | A pointer to the proof idea (detail belongs to anmath-methods) |
| Organization of the paper | Section-by-section roadmap |

## Positioning against the literature

- Name the **closest prior results** and authors explicitly; state precisely what they
  proved and where your theorem goes beyond it (stronger hypothesis removed, sharper
  constant, new range, full generality).
- Engage carefully with **priority**: cite preprints/announcements you are aware of and
  state the relationship honestly. Claiming priority without engaging the record is a
  serious referee red flag.
- Do not rely on **unpublished or unverifiable** results for the core comparison; if a
  cited result is itself unpublished, say so and isolate your dependence on it.

## Checklist

- [ ] Main Theorem is stated precisely, with all hypotheses, near the first page
- [ ] It is clear which statement is the headline vs. corollaries
- [ ] The exact advance over prior work is quantified, not just asserted
- [ ] Closest prior results are named with authors and what they proved
- [ ] Priority relative to known preprints is engaged honestly
- [ ] The statement matches exactly what the proof delivers (no over/under-claim)
- [ ] MSC subject classification chosen to match the headline result

## Anti-patterns

- Burying the main theorem on page 8 after long preliminaries
- "We prove strong results about X" with no precise statement up front
- Claiming generality the proof does not actually establish
- Vague positioning ("improving earlier work") without naming the earlier work
- Asserting priority while ignoring a known competing announcement
- Listing five "main" theorems so the actual contribution is unclear

## Output format

```
【Main Theorem (precise)】...
【What is new vs. prior】removed-hypothesis / sharper-bound / settles-conjecture / ...
【Closest prior results】author (year): proved ...
【Corollaries / reach】...
【Priority note】no conflict / relationship to preprint X is ...
【MSC classes】primary ..., secondary ...
【Next step】anmath-methods (lay out the proof architecture)
```
