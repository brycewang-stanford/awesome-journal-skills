---
name: jf-referee-strategy
description: Use when anticipating referee objections and selecting suggested/opposed reviewers before or during a The Journal of Finance (JF) submission. Plans for review; it does not write the rebuttal (use jf-rebuttal).
---

# Referee Strategy (jf-referee-strategy)

## When to trigger

- Before submitting: anticipating the objections a JF referee will raise
- The portal asks for suggested / opposed reviewers
- A conflict of interest among editors, AEs, or referees needs flagging

## How JF review works (plan around it)

JF, the AFA flagship, runs a demanding multi-round process: a handling **editor** (currently **Antoinette Schoar (MIT)**, with co-editors and 50+ Associate Editors — verify the masthead) screens first, then assigns typically **2–3 referees**. The reality is severe — **~33–45% desk-rejected, ~5% accepted** (afajof.org editor reports, accessed 2026-05-30). Most papers die at desk review, so the first job is surviving the editor, not the referees.

### JF-specific channels
- A **cover letter is normally unnecessary** at JF — use one **only** to flag a conflict of interest (referees/AEs/editors who should be excluded) or to request a code-sharing exemption. Do not pad it (see `jf-submission`).
- Suggested/opposed reviewers, if the portal asks, should be specific and justified.

## Anticipating objections (pre-empt in the paper)

| Likely referee objection            | Where to neutralize it                          |
|-------------------------------------|-------------------------------------------------|
| "This is already in [paper]"        | Contribution paragraph (`jf-literature-positioning`) |
| "Identification is not credible"    | Design section + IA tests (`jf-identification`) |
| "Just data mining / multiple testing" | Disclosed search + adjusted thresholds (`jf-robustness`) |
| "Not general-interest enough"       | Reframe for the broad AFA reader (`jf-topic-selection`) |

## Checklist

- [ ] Top 3 likely referee objections listed and pre-empted in the manuscript
- [ ] Desk-reject risk assessed (general interest, identification, fit)
- [ ] Opposed reviewers (genuine COI) noted only if the portal asks
- [ ] Cover letter used only for COI or code-exemption — otherwise omitted
- [ ] Suggested reviewers are specific and defensible

## Anti-patterns

- Writing a long cover letter JF did not ask for
- Listing opposed reviewers without a real conflict (reads as gaming)
- Ignoring desk-reject risk and over-optimizing for referees
- Leaving the obvious "already known" objection unaddressed

## Output format

```
【Top objections + where pre-empted】...
【Desk-reject risk】low / med / high — why
【COI to flag in cover letter?】yes / no
【Suggested/opposed reviewers (if asked)】...
【Next step】jf-submission → (after decision) jf-rebuttal
```
