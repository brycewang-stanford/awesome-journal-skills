---
name: lancet-reporting
description: Use to select and apply the correct EQUATOR reporting guideline for a Lancet manuscript — CONSORT for RCTs (with the mandatory flow diagram), STROBE for observational studies, PRISMA for systematic reviews/meta-analyses, SPIRIT for protocols — and to attach the completed checklist and study-flow diagram.
---

# Reporting Guidelines & Flow Diagrams (lancet-reporting)

## When to trigger

- The study type is settled and you need the matching reporting checklist.
- There is no participant flow diagram (CONSORT/PRISMA) in the manuscript.
- A reviewer or editor asks for a completed reporting checklist with page/line references.
- The manuscript mixes endpoints/numbers that the flow diagram should reconcile.

## Pick the guideline by study type (via EQUATOR)

The Lancet requires the appropriate [EQUATOR Network](https://www.equator-network.org/) reporting guideline and a completed checklist on submission.

| Study type | Guideline | Mandatory diagram |
|------------|-----------|-------------------|
| Randomized controlled trial | **[CONSORT](https://www.consort-statement.org/)** (+ extensions: cluster, non-inferiority, pragmatic, harms, PRO) | **CONSORT flow diagram** (enrollment → allocation → follow-up → analysis) |
| Observational (cohort, case-control, cross-sectional) | **[STROBE](https://www.strobe-statement.org/)** | Participant flow / selection diagram |
| Systematic review / meta-analysis | **[PRISMA](https://www.prisma-statement.org/)** (+ PRISMA-P for protocols) | **PRISMA flow diagram** (records → screened → included) |
| Trial / review **protocol** | **SPIRIT** (trials) / **PRISMA-P** (reviews) | — |
| Diagnostic accuracy | **STARD** | Patient flow |
| Prediction model | **TRIPOD** | — |
| Quality improvement | **SQUIRE** | — |
| Economic evaluation | **CHEERS** | — |

## The flow diagram is mandatory for RCTs and systematic reviews

- [ ] **CONSORT flow diagram** present for every RCT: numbers assessed for eligibility, excluded (with reasons), randomized, allocated, lost to follow-up/discontinued (with reasons), and analyzed in each arm.
- [ ] **PRISMA flow diagram** present for every systematic review/meta-analysis: records identified, duplicates removed, screened, full-text assessed, excluded (with reasons), and included.
- [ ] Every number in the flow diagram **reconciles** with Table 1, the analysis populations, and the abstract.

## Checklist discipline

- [ ] Complete the official checklist for the chosen guideline.
- [ ] Map each item to a **page and line** in the manuscript (editors and reviewers check this).
- [ ] Use the correct **extension** (e.g., CONSORT cluster for cluster-randomized trials; CONSORT harms for adverse-event reporting; CONSORT-PRO for patient-reported outcomes).
- [ ] Submit the checklist as a supplementary file.

## Equity-relevant reporting

- Apply equity-focused extensions where relevant (e.g., **PRISMA-Equity**, **CONSORT-Equity** considerations) and the **PROGRESS-Plus** framework for reporting equity-relevant participant characteristics.
- Coordinate sex/gender and race/ethnicity reporting with `lancet-ethics` (SAGER guidelines).

## Output format

```
【Study type】 RCT / observational / systematic review / protocol / other
【Guideline + extension】 CONSORT(+ext) / STROBE / PRISMA(+ext) / SPIRIT / STARD / TRIPOD / ...
【Flow diagram】 present & required? CONSORT / PRISMA / N/A  → gaps
【Flow numbers reconcile】 with Table 1 + analysis populations + abstract? yes/no
【Checklist】 completed + page/line mapped? yes/no
【Equity reporting】 PROGRESS-Plus / equity extension applied where relevant? yes/no
【Next】 lancet-statistics
```

## Anti-patterns

- **Do not** submit an RCT without a CONSORT flow diagram, or a systematic review without a PRISMA one.
- **Do not** leave flow-diagram numbers that disagree with the analysis populations or Table 1.
- **Do not** submit a checklist with "see manuscript" instead of specific page/line references.
- **Do not** use the base guideline when an extension fits the design better (cluster, non-inferiority, pragmatic, harms).
