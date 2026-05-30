---
name: restud-submission
description: Use when running the final pre-submission preflight for a The Review of Economic Studies (REStud) manuscript — anonymity, format, references, online appendix, files, and the submission portal. Last gate before submitting; does not assess the science. Verify current limits and portal on the journal's official page.
---

# REStud Submission Preflight (restud-submission)

## When to trigger

- Within 48 hours of submission
- After every R&R, before resubmission
- When unsure which files the portal requires
- After a rejection elsewhere, when routing into REStud

## Durable norms (verify current specifics)

REStud is run by The Review of Economic Studies Ltd and published by Oxford University Press. The submission rules below describe **durable conventions**; exact length limits, fees, file types, and the portal URL **change — confirm them on the journal's official author guidelines before submitting**.

- **References:** author-date (Harvard) style throughout.
- **Online appendix:** REStud uses an online appendix for full proofs, additional robustness, and supplementary material. Keep the main text lean and route detail there.
- **Replication:** data and code are required for accepted empirical papers (see `restud-replication-package`).
- **Anonymity:** REStud reviews are refereed; prepare an anonymized manuscript unless the current guidelines say otherwise.

## Format checklist

- [ ] Manuscript compiles to a single clean PDF (no tracked changes, comments, or draft watermarks)
- [ ] References in author-date style; every in-text cite appears in the list and vice versa
- [ ] Tables use professional rules; figures are vector with self-contained notes
- [ ] Equations numbered; symbols glossed on first use
- [ ] Online appendix prepared as a separate file (proofs, extra robustness)
- [ ] Main text length within the current guideline (verify on official page)
- [ ] Abstract within the current word limit (verify on official page)
- [ ] JEL codes and keywords included

## Anonymity checklist (if anonymized review)

- [ ] Author names, affiliations, and acknowledgements removed from the manuscript
- [ ] Self-citations phrased neutrally ("Smith (2020) shows", not "in our earlier work")
- [ ] File metadata stripped of author identity
- [ ] Funding / acknowledgement notes moved out of the anonymized file
- [ ] Links to personal websites / repositories that reveal identity removed or anonymized

## Files to prepare

- [ ] Main manuscript PDF (anonymized if required)
- [ ] Online appendix (proofs, supplementary robustness)
- [ ] Cover letter (only if there is substantive information — COI, data-access limits, related submissions)
- [ ] Conflict-of-interest / disclosure statement per the current policy
- [ ] Suggested / opposed referees (from `restud-referee-strategy`) if the portal asks
- [ ] Replication materials planned (required at acceptance, not necessarily at submission)

## Submission system

- REStud uses an online editorial system (commonly Editorial Express for economics journals — **confirm the current portal on the official page**).
- The corresponding author submits; ensure ORCID and contact details are current.
- A submission fee may apply and varies by membership/income group — **verify the current fee schedule on the official page**; do not quote a stale figure to the user.

## Anti-patterns

- Submitting a manuscript whose abstract exceeds the current limit "but should be fine"
- Numbered-reference style when REStud uses author-date
- Leaving author-identifying metadata or acknowledgements in an anonymized file
- A long cover letter that pitches the contribution (the abstract does that)
- Stuffing proofs into the main text instead of the online appendix
- Quoting a stale submission fee or word limit as if current — always send the user to verify

## Output format

```
【LENGTH】main text X / abstract Y — vs current limit (verify)
【ANONYMITY】pass / fixes: [...]
【REFERENCES】author-date confirmed; in-text ↔ list reconciled
【ONLINE APPENDIX】prepared / n/a
【FILES READY】[...]
【FEE / PORTAL】directed user to verify on official page
【READY TO SUBMIT】yes / no — blockers
【NEXT SKILL】await decision → restud-rebuttal
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — REStud manuscript skeleton (abstract, model/empirics structure, author-date references, online-appendix layout)
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, anonymity, exhibits, references, appendix, and portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — econ data sources and Stata / R / Python packages for REStud-track empirical and structural work
