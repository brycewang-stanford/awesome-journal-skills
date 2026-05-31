---
name: smj-rebuttal
description: Use when drafting the response letter and revising a Strategic Management Journal (SMJ) manuscript after an R&R decision. Structures the point-by-point response; it assumes the revision plan from smj-review-process is set.
---

# R&R Response & Rebuttal (smj-rebuttal)

## When to trigger

- You received a Major/Minor Revision and have revised (or are revising) the manuscript
- You need to write the response-to-reviewers letter
- You must decide how to respond to a comment you disagree with
- The manuscript changes are in progress but the response document is not yet written

> Revise the manuscript first. A response letter written before the actual edits exist will over-promise and drift from the paper.

## The response-letter structure

1. **Opening to the editor.** Thank the action editor and reviewers; state that you have revised substantially; summarize the **2–4 most important changes** (lead with how you addressed the gating concern — usually endogeneity or contribution).
2. **Point-by-point response.** For *every* comment, in order, per reviewer:
   - Quote or paraphrase the comment (verbatim is safest).
   - State your response and **exactly what changed**.
   - Point to the location: "see revised Section 4.2, pp. 18–20, and new Table 5."
3. **Reviewer-by-reviewer grouping** with clear headers (Reviewer 1, 2, …, Editor).
4. **Summary of changes** (optional) and a clean revised manuscript plus, where helpful, a tracked-changes version.

## Responding well

- **Address every comment** — none silently dropped. Even a comment you reject gets a respectful, evidence-based reply.
- **Show, don't assert.** "We now address endogeneity with an instrument (new Section 4.3) and report the first-stage F (Table 4)" beats "we believe endogeneity is not a concern."
- **Lead each reply with the action taken**, then the rationale.
- **Disagree respectfully and with evidence.** When pushing back, acknowledge the concern, present the counter-evidence or theoretical reason, and offer a compromise (e.g., a robustness check or appendix note) where possible.
- **Reconcile conflicting reviewers** explicitly; if two reviewers want opposite things, explain your choice and flag it for the editor.
- **Match tone to the editor's priorities** from the decision letter; the gating concern gets the most thorough treatment.

## SMJ-specific emphases in the response

- If the gating concern was **endogeneity**, your strongest reply is a *design* improvement (instrument, shock, matching, selection model, or partial-identification bounds) with the identification evidence shown — not more controls or rhetoric. This aligns with SMJ's own standard (Bettis, Gambardella, Helfat & Mitchell, 2014, *SMJ* 35: 949–953): a good-faith effort to address endogeneity, and **no spec-mining for better p-values** (SMJ disapproves of data snooping / p-hacking). If causation remains imperfect, reframe the claim honestly — SMJ accepts this.
- If the gating concern was **contribution**, sharpen the theoretical advance and its strategy stakes (loop back to `smj-contribution-framing`); do not merely add findings.
- Keep the manuscript's framing consistent with the letter — reviewers re-read the intro and discussion to check that promised changes actually landed.

## Checklist

- [ ] The manuscript is actually revised before the letter is finalized
- [ ] Every comment from every reviewer and the editor has a response
- [ ] Each reply states the concrete change and its location (section/page/table)
- [ ] The gating concern is addressed first and most thoroughly
- [ ] Push-backs are respectful and evidence-based, with a compromise offered where possible
- [ ] Conflicting reviewer requests are reconciled and flagged to the editor
- [ ] A clean and (if useful) tracked-changes manuscript accompany the letter
- [ ] Tone is professional and grateful throughout

## Anti-patterns

- Silently ignoring or partially answering a comment
- Asserting a concern is unfounded without new evidence (especially on endogeneity)
- Adding more control variables in place of a real identification fix the reviewer asked for
- Defensive or combative tone toward reviewers or the editor
- Promising changes in the letter that are not actually in the revised manuscript
- Letting the intro/discussion framing contradict the changes claimed in the letter
- Treating a "contribution" critique as solvable by piling on more empirical results

## Output format

```
【Decision being answered】major / minor
【Gating concern + how addressed】endogeneity → [new design] / contribution → [sharpened claim]
【Comments answered】all (n) / outstanding: [...]
【Push-backs】[comment → evidence-based reply + compromise]
【Reviewer conflicts reconciled】yes / flagged to editor
【Manuscript versions】clean + tracked
【Tone】grateful, evidence-led
【Next step】re-preflight via smj-submission, then resubmit → smj-review-process for the next round
```

## Templates & resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ endogeneity / p-hacking policy (Bettis et al. 2014) and Co-Editor roster
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — packages for added identification / robustness analyses
