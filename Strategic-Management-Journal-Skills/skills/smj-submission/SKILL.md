---
name: smj-submission
description: Use when running the final pre-submission preflight for a Strategic Management Journal (SMJ) manuscript via ScholarOne — format, anonymization, files, and cover letter. Checks readiness; it does not write the paper or the rebuttal.
---

# Submission Preflight (smj-submission)

## When to trigger

- "I'm submitting tomorrow"
- Final check before clicking submit in ScholarOne Manuscripts
- Unsure which files and metadata the system needs
- Preparing the cover letter and reviewer suggestions

## Before anything: verify the live guidelines

SMJ is published by **Wiley for the Strategic Management Society** and submitted through **ScholarOne Manuscripts**. Word limits, fee/open-access options, reference style, and required statements are periodically updated. **Verify the current Author Guidelines on the official SMJ page** before submitting — do not rely on remembered numbers. Use this skill for the durable process; confirm volatile specifics yourself.

## Manuscript readiness

- [ ] Structure complete: intro, theory & hypotheses, methods, results, discussion, references
- [ ] Contribution to strategy theory is explicit in the introduction
- [ ] Endogeneity / identification is addressed in the body (the most-scrutinized element)
- [ ] Abstract states question, approach, and finding within the journal's limit (verify count)
- [ ] Keywords selected; manuscript length within current guidelines (verify)
- [ ] Tables/figures self-contained; secondary material in an online supplement
- [ ] References complete and in the current SMJ/Wiley style; every in-text cite appears in the list and vice versa

## Anonymization (double-blind)

SMJ uses double-blind review. Before upload:

- [ ] Author names, affiliations, and acknowledgments removed from the manuscript file
- [ ] Self-citations phrased neutrally ("prior work shows (Author, 2021)"), not "in our earlier paper"
- [ ] Funding/acknowledgment details placed only where the system requests them, not in the main file
- [ ] File metadata/properties scrubbed of author identity
- [ ] File names contain no author or institution names
- [ ] No identifying data-provider or proprietary-dataset language that reveals the team

## Files & metadata in ScholarOne

- [ ] Anonymized main manuscript (with embedded or separate exhibits per guidelines)
- [ ] Title page with author details (separate, non-anonymized) if required
- [ ] Cover letter (see below)
- [ ] Online appendix / supplementary materials, if any
- [ ] Any required statements (data availability, conflict of interest, ethics) — confirm current requirements
- [ ] Suggested reviewers (and any opposed reviewers), if the system invites them
- [ ] Correct article type selected (regular article vs. any special issue)

## Cover letter

- Brief: state the title, the strategy contribution in 2–3 sentences, and why SMJ is the right outlet.
- Confirm the work is original, not under review elsewhere, and that all authors approve.
- Note any special-issue call you are responding to.
- Do not oversell or summarize the whole paper; the action editor reads the manuscript.

## Anti-patterns

- Submitting without re-checking the current word limit / format on the official page
- Leaving author identity in metadata or acknowledgments under double-blind review
- A reference list still in a default citation-manager style, not SMJ/Wiley style
- A cover letter that pitches "management" relevance instead of the strategy contribution
- Forgetting required statements (data availability / conflicts) the system mandates
- Submitting the supplement contents inside the main anonymized file when they should be separate

## Output format

```
【Guidelines verified on official page】yes / TO DO
【Anonymization】pass / fix: [...]
【Files staged】main, title page, cover letter, supplement, statements
【Reference style】SMJ/Wiley conformed / fix
【Article type】regular / special issue: [name]
【Reviewer suggestions】[n]
【Next step】smj-review-process (then smj-rebuttal on decision)
```

## Templates & resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (format, anonymization, identification, files, cover letter)
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — SMJ-style manuscript skeleton (abstract, hypotheses, variable table, identification section, references)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — strategy data sources (Compustat / CRSP / SDC / BoardEx / Orbis / patents) and Stata / R / Python packages
