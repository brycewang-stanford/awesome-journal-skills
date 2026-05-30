---
name: qje-referee-strategy
description: Use when war-gaming likely referee objections for a Quarterly Journal of Economics (QJE) manuscript before submitting, to close gaps pre-emptively. Anticipates referee reports; it does not write the post-decision response letter (see qje-rebuttal).
---

# Referee Strategy (qje-referee-strategy)

## When to trigger

- The paper is nearly submission-ready and you want to stress-test it adversarially
- You suspect a specific weakness a referee will seize on
- You are choosing what to put in the body vs. the appendix to forestall objections
- You want to draft suggested/excluded referees and a strategic cover note

## The QJE refereeing reality

QJE is **notoriously selective** with **fast desk rejection** and, for papers that survive, **few rounds with demanding referees**. The strategic implication: you usually get *one* substantive shot. The paper must be near-bulletproof at submission, because there will not be many rounds to fix fundamentals. Anticipate the report you would write if you were the toughest expert in your subfield, and answer it in advance.

## Map the three referee archetypes

| Referee type        | What they attack                                          | Pre-empt by...                                            |
|---------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| The identification hawk | The exogeneity claim; pre-trends; exclusion restriction | Falsification + placebo evidence in the body (see qje-identification) |
| The "so what?" skeptic  | Generality; whether the answer matters                  | A crisp broad-lesson + magnitude benchmarking (qje-topic-selection) |
| The mechanism doubter   | Whether the proposed channel is the real one            | A testable prediction confirmed in data (qje-theory-model) |

## War-gaming protocol

1. **Write the hostile report.** In 5–8 bullets, list the strongest objections a top expert would raise. Be ruthless; this is cheaper now than after a rejection.
2. **Triage.** For each: is it a *fundamental* threat (kills the claim) or a *robustness* request (adds a table)? Fundamentals must be resolved before submission, not deferred to R&R.
3. **Locate the answer.** For each objection, point to where in the paper it is already answered. If nowhere, add it (body for fundamentals, appendix for robustness).
4. **Decide the framing.** Pre-empt the biggest objection explicitly in the text ("A natural concern is X; we address it in three ways ..."). Showing you saw it coming builds referee trust.

## Cover-letter / referee suggestions

- Suggest referees who are expert and fair; avoid close collaborators and advisors (conflicts).
- Note genuine conflicts to exclude, briefly and professionally.
- Keep any cover note short: the question, the design, the headline result, and fit for a general-interest journal.

## Checklist

- [ ] A written hostile report exists with the 5–8 strongest objections
- [ ] Every fundamental threat is resolved in the body before submission
- [ ] Each robustness objection has a pre-emptive appendix answer
- [ ] The single biggest concern is addressed explicitly and early in the text
- [ ] Magnitudes benchmarked so the "so what?" referee is satisfied
- [ ] Mechanism prediction tested so the channel is not merely asserted
- [ ] Suggested referees are expert, fair, and conflict-free

## Anti-patterns

- Submitting with a known fundamental hole, hoping referees miss it (they will not)
- Deferring identification fixes to "future R&R" — QJE may not grant the round
- Ignoring the obvious objection rather than naming and answering it
- Suggesting collaborators/friends as referees (signals naivety or conflict)
- A long, defensive cover letter that argues instead of stating the contribution

## Output format

```
【Hostile report】[5–8 strongest objections]
【Fundamentals】[threats that must be fixed pre-submission] — status each
【Robustness asks】[appendix answers] — status each
【Pre-empted in text】the biggest concern, addressed where: ...
【Referee suggestions】[expert, fair, conflict-free]
【Next step】qje-submission
```
