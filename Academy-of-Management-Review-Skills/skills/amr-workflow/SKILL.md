---
name: amr-workflow
description: Use when deciding which amr-* sub-skill to invoke next, or when sequencing a theory-building manuscript from theoretical-puzzle framing through developmental-review revision for an Academy of Management Review (AMR) submission. Routes — does not replace — the specialized skills.
---

# AMR Theory-Building Workflow (amr-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which
amr-* skill to use at the current stage** of an Academy of Management Review manuscript.

Default assumption: unless the user says otherwise, treat the target as AMR — the Academy
of Management's premier **theory journal**. AMR publishes **conceptual articles that build
new theory**. It contains **no datasets, no hypothesis tests, no results section**. The
deliverable is a genuinely new theoretical contribution: new constructs, a new process
model, or a reconceptualization — developed with rigorous logic, explicit assumptions,
propositions, and boundary conditions. If the project has data and tests, it belongs at
AMJ / ASQ / SMJ, not AMR.

## When to trigger

- The user asks "what should I do next?" on a conceptual paper
- A draft arrives and you must locate its bottleneck (puzzle? logic? contribution?)
- Work is thrashing between theorizing, figure-building, and writing
- An AMR decision letter (developmental review) has arrived and the work shifts to revision

## Routing table

| Current symptom                                                  | Next skill                  |
|------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure there is a real theoretical puzzle       | `amr-topic-selection`       |
| Have a puzzle but constructs/relationships/logic are not built   | `amr-theory-development`    |
| Unsure which conversation to enter or what to "challenge"        | `amr-literature-positioning`|
| Propositions exist but the construction method feels thin        | `amr-methods`               |
| Propositions stated but underlying logical argument is missing   | `amr-data-analysis`         |
| Cannot articulate what is NEW vs. prior theory                   | `amr-contribution-framing`  |
| Box-and-arrow figure has no mechanism / typology not earning its keep | `amr-tables-figures`   |
| Prose reads like a literature review, not an argument            | `amr-writing-style`         |
| Ready to submit; need the ScholarOne preflight                   | `amr-submission`            |
| Want to understand AMR's developmental, multi-round review       | `amr-review-process`        |
| Received an R&R; need to write the response document             | `amr-rebuttal`              |

## Default order

1. `amr-topic-selection` — lock the theoretical puzzle (the "why doesn't existing theory explain this?")
2. `amr-literature-positioning` — identify the conversation to challenge and extend
3. `amr-theory-development` — build constructs, relationships, propositions, boundary conditions
4. `amr-methods` — theory-construction craft: construct domains, mechanisms, assumptions
5. `amr-data-analysis` — argument development: logic checks, counterfactuals, alternative explanations
6. `amr-contribution-framing` — differentiate the new theory from prior work
7. `amr-tables-figures` — finalize the conceptual figure / typology / propositions table
8. `amr-writing-style` — AOM house style; argument-driven prose (polish)
9. `amr-submission` — ScholarOne preflight
10. `amr-review-process` — understand the developmental review you are about to enter
11. `amr-rebuttal` — after the R&R

> `amr-writing-style` is a **late-stage polish**. Do not polish prose before the theory's
> logic stands up (`amr-data-analysis`) and the contribution is differentiated
> (`amr-contribution-framing`).

## Decision shortcuts

- "I have an interesting phenomenon but no theory" → `amr-topic-selection`
- "I don't know whose theory I'm arguing with" → `amr-literature-positioning`
- "I have propositions but no logic connecting them" → `amr-data-analysis`
- "My P1–P5 read like assertions" → `amr-theory-development` then `amr-data-analysis`
- "A reviewer will ask 'what's new here?'" → `amr-contribution-framing`
- "My model figure is boxes and arrows with no mechanism" → `amr-tables-figures`
- "It reads like a review essay" → `amr-writing-style`
- "I'm about to hit submit" → `amr-submission`
- "I got a Reject & Resubmit / Major Revision" → `amr-review-process` then `amr-rebuttal`

## Differences vs. AMJ / ASQ / SMJ skill stacks

If the manuscript has data, measures, and statistical tests, an empirical-management stack
(AMJ / ASQ / SMJ) fits better. The core split:

- **AMR**: builds theory; the contribution IS the theory; no data; propositions, not hypotheses tested.
- **AMJ / ASQ / SMJ**: test theory; hypotheses, samples, estimation, results.

A common failure is sending an AMR draft that is really an under-powered empirical paper,
or an AMJ draft whose "theory" is a literature summary. Pick the right stack early.

## Anti-patterns

- **Do not** skip `amr-literature-positioning` and jump to building — reviewers first ask whose conversation you are in.
- **Do not** let `amr-tables-figures` pretty up a model before the propositions and mechanisms exist.
- **Do not** let `amr-rebuttal` draft a response before the theory itself has actually been revised.
- **Do not** treat AMR as a venue for data; route empirical work elsewhere.
