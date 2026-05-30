---
name: anmath-scope-fit
description: Use when judging whether a pure-mathematics result clears the Annals of Mathematics importance and originality bar and falls within scope, before investing in framing or submission. Assesses fit and significance; does not evaluate whether the proof is correct (that is the proof's job).
---

# Scope and Significance Fit (anmath-scope-fit)

## When to trigger

- You have a finished or near-finished result and are choosing a journal
- You suspect the result may be "good but not Annals-level"
- A coauthor argues for Annals and you want an honest internal screen first
- You are unsure whether the area or style of result fits the journal

## The Annals bar (durable norms — verify specifics officially)

Annals of Mathematics publishes **major, deep results of lasting importance across all
of pure mathematics**. It is published by the Department of Mathematics at Princeton
University and the Institute for Advanced Study and is among the most selective journals
in the field. The screen is not "is this correct and new?" but "is this **important
enough** to belong in Annals?"

### Significance test — answer honestly

1. **Resolves or substantially advances a recognized problem.** Does it settle a known
   conjecture, remove a long-standing hypothesis, or break a barrier experts cared about?
2. **Lasting interest beyond a narrow subfield.** Would researchers in adjacent areas
   want to know this result exists?
3. **Depth, not just novelty.** A correct, new, but incremental result is off-fit; Annals
   favors results whose proof or consequences are deep.
4. **New method with reach.** A genuinely new technique that others will reuse can justify
   publication even when the headline theorem is modest.

If you cannot make a strong case on at least one of (1), (2), or (4), the honest call is
usually a strong specialist journal rather than Annals.

## Scope decision table

| Situation                                                     | Verdict                          |
|---------------------------------------------------------------|----------------------------------|
| Settles a well-known open problem in a core area              | In scope — strong candidate      |
| Major new technique with cross-area consequences              | In scope                         |
| Sharp improvement that experts have sought for years          | Plausible — frame significance hard |
| Solid, correct, new, but incremental within one subfield      | Off-fit — specialist journal     |
| Survey / exposition without major new theorem                 | Off-fit (Annals is not a survey venue) |
| Heavily computational with thin conceptual content            | Off-fit unless the computation settles a known problem |
| Applied / numerical with no pure-math theorem of lasting interest | Out of scope                |

## Honest self-screen before committing

- Name the specific problem or program your result advances, and the people who care.
- State, in one sentence, why this is at the level of papers Annals publishes in your area.
- Identify the strongest competing journal and articulate why Annals is the right call.
- Confirm the result is genuinely yours and not in conflict with a known preprint.

## Checklist

- [ ] I can name the recognized problem/program this advances
- [ ] I can name the communities (beyond my subfield) that will care
- [ ] The result is deep or introduces a method with reach, not merely new
- [ ] I have compared honestly against the natural specialist alternative
- [ ] No priority conflict with an existing preprint/announcement I am aware of
- [ ] I have verified current scope language on the journal's official page

## Anti-patterns

- Submitting "correct + new but incremental" and hoping the bar is lower than it is
- Confusing technical difficulty with importance — hard but uninteresting is still off-fit
- Pitching a survey or a reformulation of known results as a major advance
- Assuming a famous problem's *name* in the title substitutes for actually advancing it
- Ignoring a competing preprint that already announced the result

## Output format

```
【Result, one line】...
【Problem/program advanced】...
【Audience beyond subfield】...
【Significance basis】resolves-conjecture / new-method / removes-hypothesis / ...
【Honest verdict】Annals candidate / borderline / specialist journal
【If borderline】strengthen significance via anmath-results-framing, or redirect
【Next step】anmath-results-framing
```
