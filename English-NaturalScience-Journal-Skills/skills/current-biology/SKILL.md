---
name: current-biology
description: Use when targeting Current Biology or deciding whether a general-biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Current Biology (current-biology)

## Journal positioning

Current Biology is Cell Press's broad biology journal, covering the full range of life sciences — from molecular and cell biology through developmental biology, neuroscience, ecology, evolution, and animal behavior — with the unifying criterion that each paper must report a novel, complete advance that is interesting to biologists outside the primary specialty. Unlike the focused Cell Press sibling journals (Neuron, Immunity, Cancer Cell), Current Biology deliberately embraces cross-disciplinary scope; its dual currency is rigor plus novelty-with-breadth. The readership is biologists broadly, so a paper must carry an accessible narrative hook alongside the technical contribution.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Current Biology as the target venue.
- A study spans two or more biological disciplines and the author is unsure whether it belongs at Current Biology vs. a focused Cell Press title or PLOS Biology.
- A manuscript in evolutionary biology, ecology, or animal behavior needs to assess whether its novelty and completeness meet the Current Biology bar.
- The author needs Current Biology's desk-reject patterns and re-routing options.

## Scope & topic fit

- Evolution and evolutionary genetics: population genetics, phylogenomics, evolutionary mechanism — when the result has broad biological interest.
- Animal behavior and comparative cognition: mechanistic or computational accounts of behavior in wild or laboratory animals with clear conceptual implications.
- Ecology — from organismal to ecosystem level — when the finding delivers a conceptual advance, not just a field survey.
- Molecular and cell biology advances that are complete and significant but do not reach the focused-journal bar of Neuron, Immunity, Cancer Cell, or Developmental Cell.
- Neuroscience — sensory systems, neural computation, animal behavior — when the advance is complete but its scope is more limited than Neuron's multi-level bar.
- Developmental biology and plant biology when the advance is novel and complete, even if the model organism is niche.

## Method & evidence bar

- "Novel and complete" is the editorial standard: the key question must be answered, not merely raised; a short Report format is permitted for complete but focused advances.
- Replication and appropriate statistical power expected; ecology and behavior papers must address sample size and spatial/temporal scope.
- Mechanistic claims need experimental validation; correlational or observational studies need to be clearly framed as such and must argue for their own conceptual significance.
- Quantitative or computational methods are welcome; code/data availability expected.
- STAR Methods required for Articles; shorter Report format has condensed methods that must still be complete.
- Interdisciplinary studies should be clearly accessible to the breadth of the readership; technical jargon from one subfield should be translated.

## Structure & house style

- Two article formats: Article (full length, STAR Methods) and Report (shorter, for complete but focused results). Re-check current format definitions and limits.
- STAR Methods required for Articles; key resources table for both formats.
- Structured abstract; Cell Press "in brief" / highlights box.
- Titles should be accessible to non-specialists while being scientifically precise; avoid over-specialized terminology in the title.
- Figures should be self-explanatory to a generalist biologist; each figure panel should be labeled and the caption should enable interpretation without the text.
- The introduction must make the biological question immediately engaging to a broad readership; the contribution is stated explicitly at the end.
- Source data for all quantitative figures; data/code availability statement required.

## Official-submission checklist

- Search "Current Biology author information" on the Cell Press site and follow the current version.
- Re-check article types (Article vs. Report vs. Correspondence), length and figure limits, and supplemental policy.
- Confirm STAR Methods requirements for Articles and the condensed methods requirements for Reports.
- Re-check animal ethics, human-subjects, and field-collection permits where applicable.
- Verify data and code deposition requirements; field data should be deposited in appropriate repositories (Dryad, Zenodo, GenBank/SRA for sequencing).
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence explaining why a biologist outside this specialty would find this result interesting.
- [ ] The advance is complete: the central question is answered, not merely raised.
- [ ] The title and abstract are accessible to a generalist biologist, not only to specialists.
- [ ] Statistical power, replication, and study scope are appropriate to the claims.
- [ ] STAR Methods / condensed methods and data/code deposition are prepared.
- [ ] The framing positions the advance in a way that connects to broader biological principles.

## Common desk-reject triggers

- Advance is significant within a specialty but lacks a hook or implication for biologists outside it.
- An incomplete story: the key biological question is partially addressed, with important controls or validations missing.
- A descriptive field survey or biodiversity study without a conceptual advance.
- Study belongs in a focused Cell Press journal (Neuron, Immunity, Cancer Cell, Developmental Cell) and was submitted to Current Biology to avoid that venue's higher bar — editors recognize this.
- Methods or tool development without a biological insight — better suited to `nature-methods`.

## Re-routing decision

- Equivalent advance with greater mechanistic depth in a focused field → the relevant focused Cell Press title: `neuron`, `immunity`, `cancer-cell`, `developmental-cell`, `cell-metabolism`.
- Broad-biology advance with even broader significance → `cell`, `nature`, or `science`.
- Strong study below the Current Biology significance / completeness bar → `elife`, `plos-biology`, or the appropriate society journal (Genetics, Molecular Biology of the Cell, Behavioral Ecology).
- Ecology or evolution advance at the same tier → `nature-ecology-and-evolution` (if significance is high) or Ecology Letters (`ecology-letters`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Current Biology
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the advance novel, complete, and accessible to non-specialist biologists?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type (Article vs. Report) / length / STAR Methods / data-code deposition / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
