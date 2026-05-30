---
name: amj-submission
description: Use when running the final pre-submission preflight for an Academy of Management Journal (AMJ) manuscript — ScholarOne portal, anonymization for double-blind review, AOM house-style formatting, files, and ethics declarations. Checks readiness to submit; it does not handle the post-decision response (amj-rebuttal).
---

# Pre-Submission Preflight (amj-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires (anonymized manuscript, title page, cover materials)
- Need to confirm double-blind anonymization is complete
- Verifying the manuscript matches current AMJ/AOM formatting requirements

> Always verify current limits, fees, and required files on the official AMJ submission page and the AOM Style Guide before submitting — specifics change.

## Pre-submission checklist

### Anonymization (double-blind)

- [ ] Manuscript file contains **no** author names, affiliations, or acknowledgments
- [ ] Self-citations are worded neutrally ("prior research (Author, 2020)"), not "our earlier work"
- [ ] Acknowledgments, funding, and author bios live on a **separate title page**, not in the manuscript
- [ ] File metadata/properties scrubbed of author identity
- [ ] File names contain no author or institution identifiers

### Format (verify against the current AOM Style Guide)

- [ ] Title page (separate): title, authors, affiliations, contact, acknowledgments, funding
- [ ] Abstract within the AMJ word limit; keywords as required
- [ ] AOM/APA-style citations and reference list, alphabetized and complete
- [ ] Headings follow the AOM hierarchy; double-spaced; standard margins/font
- [ ] Tables and figures placed/numbered as the portal requires; each self-contained
- [ ] Manuscript length within current AMJ expectations (verify the page/word limit)

### Files for ScholarOne

- [ ] Anonymized main document (manuscript + tables + figures, or as the portal specifies)
- [ ] Separate title page with all identifying information
- [ ] Cover letter to the editor (concise: fit, contribution, not under review elsewhere)
- [ ] Any required supplementary/online appendix files
- [ ] High-resolution figure files if requested separately

### Declarations & ethics

- [ ] Human-subjects/IRB approval stated where applicable (separate from anonymized text)
- [ ] Data-availability/transparency statement as required by current policy
- [ ] No concurrent submission; prior conference/working-paper versions disclosed in the cover letter
- [ ] Conflicts of interest and funding disclosed on the title page
- [ ] Authorship and contribution roles agreed by all authors

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Canonical theory works for the focal domain are cited (a frequent reviewer check)
- [ ] Hypothesis labels, construct names, and table/figure numbers are consistent throughout

## ScholarOne operation notes

- AMJ submits through ScholarOne Manuscripts; create/keep your author account and ORCID current.
- Select the correct article type and the most fitting division/keywords so the manuscript routes to an appropriate action editor.
- You may be asked to suggest qualified, non-conflicted reviewers — propose people in the focal conversation without recent co-authorship.
- Upload anonymized files and the title page in the slots the system designates; preview the built PDF before final submission.

## Anti-patterns

- Submitting with self-identifying language ("in our 2019 study") intact.
- Acknowledgments/funding left inside the anonymized manuscript.
- Reference list in a non-AOM default style straight from the reference manager.
- Missing data-availability/ethics statement where the policy requires one.
- Inconsistent hypothesis labels or table numbers between text and exhibits.
- Guessing at the word/page limit instead of checking the current AMJ page.

## Output format

```
【Anonymization】pass / fix: [...]
【Format vs. AOM guide】pass / fix: [...]
【Files ready】manuscript / title page / cover letter / supplements: yes/no
【Declarations】IRB / data availability / disclosures: complete? [...]
【References】citations↔list reconciled; canonical theory cited: yes/no
【Article type & division】selected ...
【Next step】await decision → amj-review-process; on R&R → amj-rebuttal
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — full AMJ manuscript skeleton (title page, abstract, theory & hypotheses, methods, results, discussion, references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check (anonymization / format / files / declarations / measurement / tables-figures / references / portal)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — management-research data sources and analysis software (Mplus / R lavaan / HLM / Stata / SPSS PROCESS)
