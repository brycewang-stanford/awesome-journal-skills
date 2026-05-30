---
name: amr-review-process
description: Use when you need to understand the Academy of Management Review (AMR) developmental, multi-round review and interpret a decision letter focused on theoretical novelty and logical soundness. Explains the process and decision types; it does NOT draft the response document (that is amr-rebuttal).
---

# Understanding AMR's Developmental Review (amr-review-process)

## When to trigger

- You just received an AMR decision letter and need to interpret it
- You do not know what "developmental review" means or what is expected of you
- You are deciding whether an R&R is worth pursuing and how to read the editor's signals
- You need to triage reviewer comments by what AMR actually weights

## What AMR review is (durable norms)

AMR uses a **double-anonymous, multi-round, developmental** review. "Developmental" is the
operative word: the goal is to help promising theory papers become stronger, so reviews are
detailed and the bar rises across rounds. Verify current specifics on the official page, but
the durable shape is:

- A handling editor assigns the paper to several reviewers expert in your conversation.
- Reviews focus on the two things AMR exists to protect: the **novelty of the theory** and
  the **logical soundness of the argument** — not on data (there is none).
- Decisions are commonly: **Reject**; **Reject & Resubmit** (encouraged to rebuild, treated
  as a fresh submission); **Major Revision (R&R)**; less often **Minor Revision**; rarely an
  immediate **Accept**.
- An R&R is an invitation, not a promise. Multiple rounds are normal at AMR.

## Reading the decision letter

| Signal in the letter | What it usually means | Your move |
|----------------------|-----------------------|-----------|
| "Promising but the contribution is not yet clear" | Theory may be sound but under-differentiated | Re-run `amr-contribution-framing` |
| "Propositions are not well supported by the argument" | Logic gaps between premises and propositions | Re-run `amr-data-analysis`, then `amr-theory-development` |
| "Reads as a review of the literature" | No real theoretical move | Re-run `amr-literature-positioning` + `amr-writing-style` |
| "Constructs overlap existing ones" | Construct distinctiveness challenged | Re-run `amr-theory-development` (domain/distinction) |
| "Scope/level inconsistency" | Level-of-theory confusion | Re-run `amr-methods` (cross-level) |
| Editor highlights specific reviewer points as essential | The editor's priorities | Address these first and most fully |

## Triaging reviewer comments

- **Read the editor's letter as the master key.** When reviewers disagree, the editor's
  framing tells you which issues are decision-critical.
- **Separate theory-substance comments from presentation comments.** Substance (a missing
  mechanism, an undefended proposition) outranks wording.
- **Distinguish "must change the theory" from "must explain better."** Some comments mean
  the theory is wrong; others mean the prose hid a sound argument.
- **Note conflicts between reviewers** and plan to adjudicate them transparently in the
  response (handled in `amr-rebuttal`).

## Checklist

- [ ] Decision type identified (Reject / R&R / Reject & Resubmit / Minor)
- [ ] The editor's stated priorities are extracted and ranked
- [ ] Each reviewer comment tagged: theory-substance vs. presentation
- [ ] Comments mapped to the skill that addresses them (theory / logic / positioning / contribution)
- [ ] Reviewer conflicts identified for transparent adjudication
- [ ] Realistic judgment made on whether the revision can meet the raised bar

## Anti-patterns

- Treating an R&R as acceptance and making only cosmetic changes
- Ignoring the editor's letter and responding only to reviewers
- Reading "developmental" as "the reviewers will fix it for me"
- Promising in a rebuttal to add data — AMR neither wants nor accepts data
- Underestimating the number of rounds and over-claiming the revision is final

## Output format

```
【Decision type】Reject / Reject & Resubmit / Major (R&R) / Minor
【Editor's priorities】ranked list
【Comment triage】substance: [...] | presentation: [...]
【Skill mapping】comment → amr-* skill
【Reviewer conflicts】[...]
【Go / no-go】pursue revision? rationale
【Next step】amr-rebuttal
```
