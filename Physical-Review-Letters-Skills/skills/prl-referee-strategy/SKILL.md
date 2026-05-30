---
name: prl-referee-strategy
description: Use when choosing suggested and opposed referees for a Physical Review Letters submission and pre-empting the objections APS referees are likely to raise. Plans referee handling; does not write the manuscript or the rebuttal.
---

# PRL Referee Strategy (prl-referee-strategy)

## When to trigger

- The submission form asks for suggested / opposed referees
- You want to anticipate the objections a PRL referee will raise and address them in advance
- A prior Letter was bounced and you are rethinking who reviews it
- You are coordinating the cover-letter referee section (see `prl-cover-letter`)

## How PRL review works (durable shape)

PRL is **selective**. APS editors triage on importance + breadth, then send promising Letters to referees (commonly two or more). A referee can recommend rejection on **importance/breadth grounds even when the work is correct** — so your strategy must defend both the science *and* the venue fit. There are defined resubmission and appeal routes if you disagree (handled in `prl-revision`).

## Choosing suggested referees

| Principle                          | Practice                                                          |
|------------------------------------|------------------------------------------------------------------|
| Competent on the method            | Can actually judge your systematics/derivation                   |
| Spans the breadth claim            | Include someone from the neighboring field you claim to reach    |
| No conflict of interest            | Not recent collaborators, advisors, or same-institution          |
| Constructive, not partisan         | Known for fair, rigorous reports — not for reflexive PRL gate-keeping |
| Likely to grasp the significance   | Will recognize why the result is broad, not just correct         |

Suggest a small set that *together* can vouch for both correctness and breadth. Avoid stacking your suggestions only with subfield insiders, since editors may read that as evading the breadth test.

## Choosing opposed referees

- Oppose only with a brief, **professional, factual** rationale (direct competitor with a conflict, a documented dispute). Editors discount emotional or vague objections.
- Do not over-oppose; a long opposed list signals defensiveness.

## Pre-empting the likely objections (do this in the manuscript, not just the letter)

Anticipate the standard PRL referee moves and disarm them in advance:

- **"Not broad enough / belongs in Phys. Rev. B."** → Strengthen the broad-interest framing in the opening and cover letter (`prl-results-framing`, `prl-cover-letter`).
- **"An obvious artifact could explain this."** → State the decisive control inline (`prl-methods`).
- **"Incremental over Ref. [X]."** → Make the qualitative advance explicit; cite and differentiate.
- **"Can't follow it without the SM."** → Ensure the Letter stands alone (`prl-supplementary`).
- **"Over-claimed."** → Calibrate claims to evidence (`prl-writing-style`).

## Checklist

- [ ] Suggested referees can judge both correctness and breadth
- [ ] At least one suggested referee represents the claimed neighboring audience
- [ ] No conflicts of interest among suggestions
- [ ] Opposed referees (if any) have a brief, factual, professional rationale
- [ ] The opposed list is short
- [ ] The manuscript already pre-empts the top 3 likely objections
- [ ] Cover-letter referee section is consistent with the submission form

## Anti-patterns

- Suggesting only close-network insiders (reads as breadth evasion)
- Opposing referees with emotional or unsubstantiated reasons
- A long opposed list that signals defensiveness
- Suggesting a recent collaborator (conflict) as an "independent" referee
- Ignoring the breadth objection and hoping the science alone carries it

## Output format

```
【Suggested referees】N — cover correctness + breadth?  yes / adjust
【Neighboring-field referee included】yes / add
【Conflicts checked】clean / fix
【Opposed referees】N (short) — factual rationale?  yes / fix
【Top objections pre-empted in manuscript】broad-fit / artifact / increment / stand-alone / over-claim
【Next】prl-submission (enter referees) → later prl-revision
```

> Referee count, suggestion limits, and form fields evolve — verify on the official APS / PRL author page.
