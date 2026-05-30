---
name: asq-workflow
description: Use when deciding which asq-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Administrative Science Quarterly (ASQ) manuscript. Routes — it does not replace — the specialized skills.
---

# Administrative Science Quarterly Workflow (asq-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which asq-* skill to use at your current stage**.

Default assumption: unless the user says otherwise, treat the target as **Administrative Science Quarterly (ASQ)** — a top, theory-driven journal in organization theory and the sociology of organizations, published by SAGE in association with the Samuel Curtis Johnson Graduate School of Management at Cornell University. ASQ's hallmark is a deep, often *surprising* theoretical insight about organizations, delivered with superb craft. It publishes **both** rigorous quantitative work **and** rich qualitative/inductive studies (grounded-theory, ethnographic, historical) — method follows the theoretical question.

## When to trigger

- The user asks "what should I do next?"
- The user drops a draft and needs the current bottleneck diagnosed
- Work keeps ping-ponging between theory, methods, and prose with no clear state
- An ASQ decision letter arrived and the user needs to switch into review/rebuttal mode

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is interesting but not yet *surprising*; unsure it fits ASQ        | `asq-topic-selection`       |
| Have a phenomenon but no theoretical engine / mechanism                 | `asq-theory-development`    |
| Lit review reads like a list; not in dialogue with org-theory traditions| `asq-literature-positioning`|
| Unsure whether design should be qualitative or quantitative; rigor gaps | `asq-methods`               |
| Have data but coding/analysis is opaque; no data-to-theory link         | `asq-data-analysis`         |
| Can't state the contribution as a "so-what" for organization theory     | `asq-contribution-framing`  |
| Tables/figures are dense or do not show the data structure (qual or quant)| `asq-tables-figures`      |
| Prose is flat, jargon-heavy, or "variance-speak" where process is needed | `asq-writing-style`         |
| Preparing to submit; need a preflight checklist                         | `asq-submission`            |
| Want to understand ASQ's developmental review before/after submitting   | `asq-review-process`        |
| Received an R&R and need to write the response                          | `asq-rebuttal`              |

## Default order

1. `asq-topic-selection` — lock the *puzzle* and the surprising organizational insight
2. `asq-theory-development` — build the theoretical engine (process or variance) before data work
3. `asq-literature-positioning` — situate in organization-theory conversations
4. `asq-methods` — choose and justify design (qualitative or quantitative); set the rigor bar
5. `asq-data-analysis` — execute analysis and the data-to-theory link
6. `asq-contribution-framing` — sharpen the theoretical "so what" once results exist
7. `asq-tables-figures` — finalize data tables, data-to-theory tables, models, figures
8. `asq-writing-style` — full-manuscript prose and craft polish
9. `asq-submission` — pre-submission preflight
10. `asq-review-process` — understand the developmental, multi-round process
11. `asq-rebuttal` — after the R&R decision

> `asq-writing-style` and `asq-tables-figures` are **late-stage polish** — do not run them while the theoretical contribution is still unsettled. At ASQ, craft cannot rescue a thin idea.

## Decision heuristics

- "I have a result but no surprise" → `asq-topic-selection`
- "My theory is a box-and-arrow model with no mechanism" → `asq-theory-development`
- "My lit review cites everyone but argues with no one" → `asq-literature-positioning`
- "I ran hypotheses but learned nothing new about organizations" → `asq-theory-development` then `asq-contribution-framing`
- "My informant quotes are decorative, not evidentiary" → `asq-data-analysis`
- "Reviewer says 'this is a method in search of a theory'" → `asq-contribution-framing`
- "I'm about to submit tonight" → `asq-submission`
- "I got a high-risk R&R with three reviewers" → `asq-review-process` then `asq-rebuttal`

## Differences vs. other management packs

- **ASQ**: theory first; *surprise* and craft are paramount; qualitative/inductive work is fully first-class; process theory is common.
- **AMJ**: empirical, hypothesis-testing norm dominates; strong quantitative bar.
- **AMR**: theory-only; no data at all.
- **SMJ**: strategy-focused; performance outcomes central.

If the manuscript is a pure conceptual paper with no data, an AMR-style stack fits better. If it is a hypothesis-testing study with no theoretical surprise, reconsider whether ASQ is the right home.

## Anti-patterns

- **Do not** skip `asq-theory-development` and rush to data — at ASQ the contribution is theoretical, not methodological.
- **Do not** let `asq-tables-figures` polish exhibits before the contribution is settled.
- **Do not** let `asq-rebuttal` draft a response letter before the manuscript itself has been revised.
- **Do not** assume "more sophisticated method" substitutes for a new organizational insight.
