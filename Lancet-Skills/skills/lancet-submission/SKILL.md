---
name: lancet-submission
description: Use as the final preflight before submitting to The Lancet — a complete checklist across importance, registration, reporting guideline + flow diagram, statistics, structured abstract, the Research in context panel, ethics/declarations/data-sharing, and required files. Bundles a checklist and a cover-letter template.
---

# Submission Preflight (lancet-submission)

## When to trigger

- The manuscript is "done" and you are about to upload.
- You want a single gate that confirms every other lancet-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Importance & framing
- [ ] Clears the importance / global-relevance / practice-or-policy bar (`lancet-fit` rung ≥ 3).
- [ ] Equity/global-health angle articulated where relevant.
- [ ] Title declarative and specific; reflects design (e.g., "a randomised controlled trial").

### Registration & design
- [ ] Trial **registered prospectively**; registration number in the **abstract** and Methods.
- [ ] Protocol + pre-specified **SAP** available; primary outcome matches the registered one.
- [ ] RCT: randomisation, allocation concealment, blinding, ITT — described.

### Reporting guideline & flow diagram
- [ ] Correct EQUATOR guideline (CONSORT / STROBE / PRISMA / SPIRIT / ...) with completed checklist, page/line-mapped.
- [ ] **Flow diagram** present (CONSORT for RCT, PRISMA for review); numbers reconcile with Table 1 and analysis populations.

### Statistics
- [ ] Effect estimates with **95% CI**; exact P; absolute + relative effects (NNT where relevant).
- [ ] Pre-specified primary analysis; ITT primary + per-protocol sensitivity; missing-data handling.
- [ ] Multiplicity strategy for secondary endpoints; subgroups pre-specified + interaction tests.

### Structured abstract
- [ ] ≤300 words under **Background, Methods, Findings, Interpretation, Funding** (exact headings).
- [ ] Registration number in Methods; primary outcome with effect size + 95% CI; funder named.

### Research in context panel
- [ ] All three parts present (Evidence before / Added value / Implications).
- [ ] "Evidence before this study" documents a systematic search (databases + terms + dates).

### Figures & tables
- [ ] Table 1 baseline characteristics (no baseline P in an RCT).
- [ ] Kaplan–Meier with numbers at risk / forest plot / map — as the design warrants; CIs shown.

### Ethics, declarations & data
- [ ] Ethics approval + consent (all sites) + Declaration of Helsinki.
- [ ] **Declaration of interests** for all authors (ICMJE).
- [ ] **Role of the funding source** statement (funder role + data access + final responsibility to submit).
- [ ] **Data sharing statement** (ICMJE-compliant for trials).
- [ ] ICMJE author contributions (incl. who verified the data); SAGER sex/gender + equity reporting; PPI statement.

### References & required files
- [ ] References within budget (~30 for an Article), correct style; all in-text citations resolve.
- [ ] Main text (IMRaD + panel), abstract, tables, figures + legends, appendix/supplement.
- [ ] Reporting checklist; protocol/SAP; cover letter; authors/affiliations/ORCIDs; corresponding author.

## Final integrity sweep

- [ ] No over-claiming: causal language matches design; no superiority claim from a non-inferiority trial.
- [ ] All abstract / flow-diagram / Table 1 / text numbers reconcile.
- [ ] Registration number, ethics references, and any data-repository identifiers are correct and live.
- [ ] Headings are **Findings / Interpretation** (not Results / Conclusions).

## Templates

- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — clinical/global-importance cover-letter scaffold.

## Output format

```
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / abstract / panel / figures+tables / reporting checklist / protocol+SAP / cover letter / declarations
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | lancet-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload a trial that lacks prospective registration without flagging it.
- **Do not** submit an RCT without a CONSORT flow diagram or a review without a PRISMA one.
- **Do not** skip the role-of-the-funding-source or data-sharing statements.
- **Do not** rely on memory; run the checklist top to bottom.
