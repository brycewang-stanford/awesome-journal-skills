---
name: sci-submission
description: Use as the final preflight before submitting to Science — a complete checklist across significance, format, figures, statistics, data, references, and required files. Bundles templates.
---

# Submission Preflight (sci-submission)

## When to trigger

- The manuscript is "done" and you're about to upload.
- You want a single gate that confirms every other sci-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Significance & framing
- [ ] Clears the broad-significance / general-interest bar (`sci-fit` rung ≥ 3).
- [ ] One-sentence advance present and demonstrated (not asserted).
- [ ] Title is declarative, specific, < ~90 characters.

### Format & length
- [ ] Format chosen (Report ~2,500 w / ≤4 items, or Research Article ~4,500 w / ≤6 items).
- [ ] Main-text word count within budget; Methods in Supplementary (for Reports).
- [ ] Results ordered by argument, claim-first paragraphs.

### Abstract & summary
- [ ] One-sentence summary ≤ ~125 characters, not a title paraphrase.
- [ ] Abstract ≤ ~125 words, no subheadings/citations, ≥1 quantified result.

### Figures & display items
- [ ] Within item budget; sized to 5.5/12/18 cm; fonts ≥ 6 pt.
- [ ] Data shown (points + n); error bars defined; scale bars present.
- [ ] Colorblind-safe; uncropped key blots + source data retained.

### Statistics & reproducibility
- [ ] Each claim: effect size + CI + n + test + assumptions.
- [ ] Biological vs technical replication clear; sample-size rationale stated.
- [ ] Randomization/blinding reported or justified; multiplicity controlled.
- [ ] Analysis code public + archived (DOI).

### Data, materials, ethics
- [ ] Data deposited with accession numbers/DOIs (no "on request" for primary data).
- [ ] Data-availability statement drafted and compliant.
- [ ] Materials/reagent sharing plan; ethics approvals (IRB/IACUC/permits) as needed.

### References
- [ ] Science numbered style, ordered by appearance, one continuous list (incl. SM).
- [ ] Full author lists; journal abbreviations; all in-text numbers resolve.

### Required files & metadata
- [ ] Main text (with title, one-sentence summary, abstract, refs).
- [ ] Figures at required resolution + figure legends.
- [ ] Supplementary Materials (Materials and Methods, supp figs/tables, captions).
- [ ] Cover letter (significance-forward).
- [ ] Author list, affiliations, ORCIDs, corresponding author.
- [ ] Author contributions (CRediT), competing interests, funding.
- [ ] Suggested/opposed reviewers (if used).

## Final integrity sweep

- [ ] No over-claiming beyond the evidence (re-read the abstract and last paragraph).
- [ ] Every figure's n, error bar, and test are defined in its legend.
- [ ] All accession numbers/DOIs are live and correct.
- [ ] Manuscript is anonymized only if double-blind is requested (Science is typically single-blind — confirm).

## Templates

- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — significance-forward cover letter scaffold.

## Output format

```
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+legends / SM / cover letter / metadata
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | sci-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload before accession numbers/DOIs exist.
- **Do not** skip the integrity sweep — over-claiming is a top rejection reason post-review.
- **Do not** rely on memory; run the checklist top to bottom.
