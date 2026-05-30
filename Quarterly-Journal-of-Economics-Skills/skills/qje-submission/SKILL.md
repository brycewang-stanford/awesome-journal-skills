---
name: qje-submission
description: Use when running the final pre-submission preflight for the Quarterly Journal of Economics (QJE) via Editorial Express — manuscript format, anonymization, references, fee, and supplementary files. Final checks; it does not draft content.
---

# Submission Preflight (qje-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit
- Unsure which files Editorial Express expects
- Confirming format, anonymization, and reference style are QJE-compliant
- Checking fee, declarations, and supplementary-materials requirements

## Process facts (verify current specifics on the official page)

- QJE is published by **Oxford University Press**, edited historically out of Harvard, and is one of the **top-5** general-interest economics journals.
- Submission is through **Editorial Express** (the AEA-ecosystem portal). Confirm the exact submission URL in the current author guidelines.
- A **submission fee** applies. The exact amount changes — **verify the current fee** before paying; fee waivers/reductions sometimes exist for specific cases.
- **Data and code replication materials** are required for accepted empirical papers; verify the current deposit/data-editor policy (see `qje-replication-package`).
- The journal is **highly selective with fast desk rejection** — a clean, complete submission is part of clearing the editor's first screen.

## Preflight checklist

### Format & style

- [ ] References in **author-date** style throughout, consistent and complete
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] Long manuscripts are acceptable; an extensive **online appendix** is expected
- [ ] Math/notation defined once; equations numbered where referenced
- [ ] PDF compiles cleanly; figures legible at print resolution

### Anonymization (if double-blind / per current policy)

- [ ] No author names, affiliations, or acknowledgments in the manuscript file
- [ ] Self-citations phrased neutrally ("Smith (2020) shows", not "in our earlier work")
- [ ] File metadata/properties scrubbed of author identity
- [ ] Acknowledgments and funding info supplied separately, not in the body

### Files for Editorial Express

- [ ] Main manuscript PDF (with embedded figures/tables)
- [ ] Online appendix (separate file)
- [ ] Cover letter (concise: question, design, headline result, general-interest fit)
- [ ] Suggested / excluded referees prepared (expert, fair, conflict-free)
- [ ] Replication materials staged for the accepted stage (see qje-replication-package)

### Declarations & fee

- [ ] Conflict-of-interest / disclosure statement per current policy
- [ ] Funding and data-source disclosures prepared
- [ ] Submission fee confirmed (verify current amount) and payment method ready
- [ ] Confirmed the paper is not under review elsewhere

### Final content sanity

- [ ] Abstract states the finding with a number (see qje-writing-style)
- [ ] Identification diagnostics complete (see qje-identification, qje-robustness)
- [ ] No over-claiming beyond what the design supports

## Anti-patterns

- Submitting with mixed/inconsistent reference styles (not clean author-date)
- Leaving author identity in self-citations or file metadata under double-blind
- Forgetting to budget/verify the current submission fee
- A defensive, multi-page cover letter instead of a tight pitch
- Submitting a thin appendix to a journal that expects an extensive one

## Output format

```
【Reference style】author-date, consistent? [Y/N]
【Anonymization】body + metadata clean? [Y/N / NA]
【Files staged】manuscript / appendix / cover letter / referees? [Y/N each]
【Fee】current amount verified + ready? [Y/N]
【Declarations】COI / funding / data prepared? [Y/N]
【Content sanity】abstract states finding; identification complete? [Y/N]
【Next step】await decision → qje-rebuttal on R&R
```

## Supplementary resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — QJE-oriented manuscript skeleton (abstract, intro arc, design, exhibits, author-date references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for credible-design empirical micro
