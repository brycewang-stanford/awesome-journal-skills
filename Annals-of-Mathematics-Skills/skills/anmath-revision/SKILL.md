---
name: anmath-revision
description: Use when responding to an Annals of Mathematics referee report — revising the manuscript to close gaps or strengthen results and writing a point-by-point reply. Drafts the revision and response after the text is fixed; does not invent significance the result lacks (see anmath-scope-fit).
---

# Revision and Response (anmath-revision)

## When to trigger

- A referee report has arrived (revision requested, or queries to address)
- A referee found a gap, a questionable step, or a missing citation
- You need to revise the manuscript and write a point-by-point reply
- A correction is needed and you must show exactly what changed

> Math reviews are slow and thorough. A report may identify a genuine gap; the right
> response is to **fix the mathematics first**, then explain — never to argue a gap away.

## Order of operations

1. **Fix the text first.** Resolve every gap, error, or imprecision in the manuscript
   before drafting a single line of reply. The reply describes changes that already exist.
2. **Triage the report.** Classify each point: (a) genuine gap/error — must fix; (b)
   request for clarification — add exposition; (c) disagreement — respond with a precise
   mathematical argument, respectfully.
3. **Verify the fix does not break anything.** A repaired step must be re-checked against
   the whole argument (re-run the self-adversarial pass from anmath-referee-strategy).
4. **Then write the reply**, point by point, pointing to exact locations in the revision.

## Point-by-point reply structure

| Element | Content |
|---------|---------|
| Opening | Brief thanks; summary of the main changes |
| Each point | Quote the referee remark, then state the change and where it appears (section/line/Lemma) |
| Gaps/errors | Acknowledge plainly, give the corrected argument, point to the new text |
| Disagreements | A precise, courteous mathematical rebuttal; concede where the referee is right |
| Marked-up version | Provide a `latexdiff` PDF so changes are easy to verify |

## Handling a real gap

- If the gap is **fixable**, fix it fully and show the new argument; do not paper over it.
- If the fix **weakens the theorem** (e.g. an extra hypothesis is needed), state the new,
  correct theorem honestly and explain the change — a correct weaker result beats a wrong
  strong one.
- If the gap is **not fixable**, the honest course may be withdrawal or a substantially
  scaled-back result; consult anmath-scope-fit on whether the salvaged result still fits.
- Never respond to a gap with "it is easy to see" — that is what created the problem.

## Tone and conduct

- Respectful and precise. Referees give a great deal of unpaid time on long reviews.
- Concede points the referee gets right; defend points you are sure of with mathematics,
  not assertion.
- Address **every** point; silence on a remark reads as evasion.

## Checklist

- [ ] Every referee point is classified (gap / clarification / disagreement)
- [ ] All genuine gaps and errors are fixed in the manuscript first
- [ ] Each fix re-checked against the whole argument (no new gap introduced)
- [ ] Reply addresses every point, pointing to exact locations in the revision
- [ ] Any weakened/corrected theorem is stated honestly with the change explained
- [ ] A `latexdiff` marked-up version is included
- [ ] Tone is respectful; defenses are mathematical, not rhetorical
- [ ] If unfixable, scope/withdrawal reconsidered via anmath-scope-fit

## Anti-patterns

- Writing the reply before actually fixing the mathematics
- Arguing a genuine gap away instead of repairing it
- Patching a gap with "it is easy to see" — the original sin, repeated
- Silently ignoring a referee remark you find inconvenient
- Claiming the original (now-known-wrong) theorem still holds without a valid proof
- Defensive or dismissive tone toward a careful, time-intensive review

## Output format

```
【Report points】N total → gaps: a; clarifications: b; disagreements: c
【Gaps fixed】point i: corrected by ..., now in §...
【Theorem changed?】no / now reads ... (honest restatement)
【Re-check after fix】no new gap / FIX
【Reply drafted】point-by-point, with locations
【latexdiff attached】yes
【If unfixable】reconsider via anmath-scope-fit
【Next step】resubmit revision + response
```
