---
name: jpe-submission
description: Use when running the final pre-submission preflight for a Journal of Political Economy (JPE) manuscript via Editorial Express — manuscript format, author-date references, submission fee, anonymity (if double-blind), exhibits, and supplementary files. Final mechanical gate; it does not improve the economic argument.
---

# Submission Preflight (jpe-submission)

## When to trigger

- "Submitting tomorrow" — the last mechanical check before pressing submit
- Unsure what the Editorial Express portal requires as separate files
- Confirming format, references, and fee handling are correct

> JPE is published by the University of Chicago Press and processed through the **Editorial Express** submission system. A **submission fee applies** and a data/code policy governs accepted papers. Fee amount, fee waivers, exact word/format limits, and whether review is double-blind change over time — **verify the current author guidelines and fee on the journal's official page before submitting.** Everything below is the durable structure of a JPE submission.

## Pre-submission checklist

### Format
- [ ] Manuscript is a single PDF, double-spaced, with figures/tables either embedded or at the end per current guidelines
- [ ] Sections ordered logically (intro → model/theory → data → strategy → results → mechanisms/robustness → conclusion)
- [ ] Equations numbered and referenced as "equation (n)"
- [ ] Figures legible in grayscale; tables self-contained with full notes
- [ ] Online appendix prepared as a separate file (proofs, full robustness, descriptive tables)

### References (house style)
- [ ] **Author-date** citations throughout — not numbered/bracket
- [ ] Reference list complete and consistently formatted (Chicago/UChicago Press style)
- [ ] Every in-text citation appears in the list; every list entry is cited
- [ ] Canonical theory the paper engages is cited (a frequent referee snag)

### Anonymity (if the journal is operating double-blind — verify)
- [ ] Author identities removed from the manuscript file and PDF metadata
- [ ] Self-citations phrased neutrally ("Smith (2020) shows..." not "in our earlier work")
- [ ] Acknowledgments / funding / institutional info on a separate title page, not in the blinded manuscript

### Fee & policy
- [ ] Submission fee amount confirmed on the official page and payment ready (check for waivers/discounts)
- [ ] Data and code availability policy reviewed; replication package staged (see `jpe-replication-package`)
- [ ] Not under review elsewhere; no duplicate/overlapping submission

### Exhibits & supplementary
- [ ] Main-text exhibits report economic magnitudes, not stars alone
- [ ] Online appendix complete and referenced from the main text
- [ ] Any restricted-data documentation prepared

### Author info & metadata
- [ ] Title, abstract, JEL codes, and keywords entered in the portal
- [ ] All co-authors and affiliations correct; corresponding author set
- [ ] Suggested referees (and any opposed referees) prepared with brief justification

## Editorial Express operational notes

- Register/log in to Editorial Express; have title, abstract, JEL codes, and the PDF ready before starting.
- Upload the manuscript PDF; attach the online appendix and cover letter as the portal requests.
- Complete the fee step; submission is typically not forwarded to editors until the fee clears.
- Confirm the submission acknowledgment email and manuscript number arrive.

## Anti-patterns

- Pulling an all-nighter and skipping the anonymity / metadata scrub
- Numbered citations left in from a different journal's template (wrong house style)
- Forgetting the submission fee step, so the paper never reaches an editor
- Funding/acknowledgments left in a blinded manuscript
- JEL codes or keywords omitted in the portal
- Online appendix referenced in text but not uploaded

## Output format

```
【Format】single PDF, double-spaced, exhibits OK? [y/n]
【References】author-date verified; list complete? [y/n]
【Anonymity】scrubbed? (or N/A — verify blinding)
【Fee】amount confirmed + ready? [y/n]
【Replication】staged per policy? [y/n]
【Portal metadata】title/abstract/JEL/keywords/referees entered? [y/n]
【Next】await decision / on R&R → jpe-rebuttal
```

## Bundled resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JPE manuscript skeleton (section order, author-date references, variable table)
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, references, anonymity, fee, exhibits, and portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — economics data sources and Stata / R / Python packages for identification, structural estimation, and replication
