---
name: jacs-workflow
description: Use when deciding which jacs-* sub-skill to invoke next, or when sequencing a Journal of the American Chemical Society (JACS) manuscript from scope check through revision. Routes — it does not replace — the specialized skills.
---

# JACS Workflow Router (jacs-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which
jacs-* skill to use for your current stage** of a JACS manuscript.

Default assumption: unless the user says otherwise, the target is the
**Journal of the American Chemical Society (JACS)** — a premier, broad-scope ACS
chemistry journal. The bar is a significant, rigorously characterized chemical
advance of broad interest, with claims fully supported by data and controls.

## When to trigger

- "What should I do next?" on a chemistry manuscript
- A draft arrives and you must find the current bottleneck (story, data, format)
- Work is bouncing between synthesis, characterization, figures, and writing
- Referee reports arrived and you need to switch into response/revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure whether the advance is broad/significant enough for JACS vs a specialized ACS journal | `jacs-scope-fit` |
| Have results but the "so what" / chemical advance is not sharp | `jacs-results-framing` |
| Synthesis or characterization may be incomplete (purity, NMR, HRMS, X-ray, controls) | `jacs-methods` |
| Schemes/spectra/structures don't look like ACS style or don't carry the story | `jacs-figures` |
| Supporting Information missing procedures, spectra copies, CIFs, or CCDC numbers | `jacs-supplementary` |
| Prose is vague, over-claimed, or not in ACS house style | `jacs-writing-style` |
| Unsure whether to write an Article or a Communication / over length | `jacs-length-management` |
| Need a cover letter stating the advance and fit | `jacs-cover-letter` |
| Ready to submit; need the Paragon Plus preflight checklist | `jacs-submission` |
| Suggesting/excluding reviewers, anticipating referee objections | `jacs-referee-strategy` |
| Decision letter / referee reports arrived; need a response strategy | `jacs-revision` |

## Default order

1. `jacs-scope-fit` — confirm broad interest and the right ACS venue/format
2. `jacs-results-framing` — pin the chemical advance and its significance
3. `jacs-methods` — synthesis + full characterization and control/mechanism rigor
4. `jacs-figures` — schemes, spectra, structures, mechanism figures (ACS style)
5. `jacs-supplementary` — build the SI (procedures, data, spectra, CIFs/CCDC)
6. `jacs-writing-style` — ACS house style and claim discipline
7. `jacs-length-management` — Article vs Communication; meet ACS format norms
8. `jacs-cover-letter` — advance + fit statement to the editor
9. `jacs-submission` — Paragon Plus preflight
10. `jacs-referee-strategy` — reviewer suggestions + objection pre-empting
11. `jacs-revision` — after the decision letter

> `jacs-writing-style` and `jacs-length-management` are **late-stage polish** —
> do not run them before the data and the advance are solid.

## Decision shortcuts

- "Is this big enough for JACS?" → `jacs-scope-fit`
- "I have data but no headline" → `jacs-results-framing`
- "A reviewer could say my new compound isn't fully characterized" → `jacs-methods`
- "My mechanism is asserted, not tested" → `jacs-methods` (controls/kinetics/labeling)
- "My scheme is ugly / spectra unreadable" → `jacs-figures`
- "Where do the CIFs and FID copies go?" → `jacs-supplementary`
- "Communication or Article?" → `jacs-length-management`
- "Submitting tomorrow" → `jacs-submission`
- "Got three referee reports" → `jacs-revision`

## Differences vs. specialized ACS journal stacks

If the work is narrow in scope (e.g., a single subfield advance with limited
cross-chemistry interest), a specialized ACS journal (*Org. Lett.*, *Inorg.
Chem.*, *Chem. Mater.*, *ACS Catal.*, *J. Org. Chem.*, etc.) may fit better.
`jacs-scope-fit` makes that call explicit. JACS rewards advances that matter
**across chemistry**, not only within one community.

## Anti-patterns

- **Do not** skip `jacs-scope-fit` — editors triage on broad interest first.
- **Do not** let `jacs-figures` polish schemes before the characterization (`jacs-methods`) is complete.
- **Do not** let `jacs-revision` draft a response before you have actually done the new experiments/edits.
