---
name: the-lancet-oncology
description: Use when targeting The Lancet Oncology or deciding whether a clinical oncology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Lancet Oncology (the-lancet-oncology)

## Journal positioning

The Lancet Oncology is a flagship specialty title in the Lancet family and one of the world's most prestigious clinical oncology journals, published by Elsevier. It publishes practice-changing cancer clinical trials, oncology policy, cancer epidemiology, and translational cancer research that is directly relevant to the clinical management of cancer at a global level. The journal maintains the Lancet family's editorial standards: rigorous trial registration, CONSORT compliance, equity and global-health consciousness, and a bias toward findings that shift oncology practice or inform cancer policy. Studies that are methodologically sound but incremental—small improvements in surrogate endpoints, single-arm studies without historical context, or descriptive epidemiology without actionable implications—are unlikely to succeed here.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Lancet/Elsevier site or submission system.

## When to trigger

- The author names The Lancet Oncology as the target venue for a phase III cancer trial, cancer epidemiology analysis, or oncology-policy paper.
- A cancer clinical trial has results that could change standard of care across a patient population at international scale.
- A cancer-burden or cancer-control analysis has policy implications for global or regional oncology systems.
- The author needs The Lancet Oncology's desk-reject risks and credible alternatives before submitting.

## Scope & topic fit

- Phase III and large phase II randomised controlled trials in any cancer type with patient-centred primary endpoints (overall survival, progression-free survival with mature data, quality of life).
- First-in-class drug approvals, definitive biomarker-selected trial results, and adaptive or platform trial designs with practice-changing results.
- Cancer epidemiology: global cancer burden, incidence and mortality trends, population-level cancer screening effectiveness.
- Oncology policy and health-systems research: cancer control in LMICs, access to cancer medicines, treatment guidelines at population scale.
- Precision oncology: biomarker-defined patient populations, molecular tumour boards, genomic stratification with clinical outcome data.
- Translational findings from trials: correlative biomarker data within a practice-changing clinical trial, not standalone discovery.

## Method & evidence bar

- Randomised trials must be pre-registered (ClinicalTrials.gov or ISRCTN or equivalent), CONSORT-compliant in full including a CONSORT flow diagram, and powered for a clinically meaningful primary endpoint.
- Phase II single-arm studies are published only when they establish a new standard for a rare tumour type or a breakthrough clinical signal with regulatory-approval implication.
- Systematic reviews and meta-analyses of cancer trials require PRISMA adherence, PROSPERO registration, and GRADE evidence profiling.
- Survival analyses must report hazard ratios with confidence intervals, Kaplan-Meier curves with patients-at-risk tables, and median follow-up duration.
- Biomarker and molecular analyses embedded within trials must follow pre-specified analysis plans; exploratory correlative data should be clearly labelled as hypothesis-generating.
- Ethics approval, independent data-safety monitoring board (for phase III trials), and informed consent are mandatory; ICMJE authorship and competing-interests disclosure are required.

## Structure & house style

- The Lancet Oncology uses a structured abstract (background, methods, findings, interpretation) followed by a funding statement; the Interpretation sentence must state the clinical implication directly.
- An "Added value of this study" summary panel (what is already known, what this study adds) is required; it must be specific to this trial's contribution—generic claims are rejected.
- Opening paragraphs should establish the unmet clinical need and the current standard of care that this study addresses or surpasses.
- Kaplan-Meier figures are standard; ensure they include patients-at-risk tables; colour-blind-accessible palettes are expected.
- Statistical reporting must include absolute differences in survival rates at landmark timepoints in addition to hazard ratios; minimise sole reliance on relative-effect measures.
- Ancillary oncology-specific content: subgroup forest plots must note that subgroup analyses are exploratory unless pre-specified.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The Lancet Oncology information for authors" and follow the current Elsevier/Lancet version.
- Re-check article type, current word/abstract/figure limits, and the "Added value" panel format.
- Confirm trial registration number, ethics approval reference, independent data-safety monitoring board statement (phase III), and informed consent are documented.
- Submit CONSORT checklist (or PRISMA for reviews) as a supplementary file with page-number citations.
- Re-check data-sharing statement: what IPD or summary data will be shared, when, via which platform, and under what access conditions.
- Re-check competing-interests declaration, funding disclosure (industry vs. academic funding independence), ICMJE author-contribution statement, and AI-use disclosure.
- Re-check open-access/APC and licensing options; preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating which current standard-of-care this study supersedes or complements, and for which patient population.
- [ ] The CONSORT flow diagram is prepared; patients at risk are shown in survival curves; hazard ratios and landmark survival rates are both reported.
- [ ] The "Added value" panel is specific: what existing evidence was incomplete and what this study conclusively establishes.
- [ ] Biomarker or subgroup analyses are clearly labelled as pre-specified or exploratory.
- [ ] Trial registration, ethics, and data-sharing statement are complete.
- [ ] All competing interests (especially industry support) are fully declared with clear statement of sponsor role in design, analysis, and publication.

## Common desk-reject triggers

- Phase II single-arm trial in a common tumour type without a compelling unmet-need or breakthrough-designation rationale.
- CONSORT flow diagram missing; primary endpoint differs from the registered endpoint without transparent amendment explanation.
- Survival analyses without patients-at-risk tables or with immature follow-up that prevents meaningful interpretation.
- Competing-interests disclosure that is incomplete or where the sponsor conducted the primary statistical analysis with no independent verification.
- "Added value" panel that is generic or repeats the abstract rather than specifying what this study adds relative to existing evidence.
- Biomarker or translational paper without a clinical trial anchor—purely preclinical or discovery studies belong in disease-biology journals.

## Re-routing decision

- Same trial but more broadly generalised to all medicine beyond oncology → `the-lancet`.
- ASCO-sponsored or US-focused oncology trial seeking society-journal publication → `journal-of-clinical-oncology`.
- Mechanistic cancer-biology study underlying the clinical finding → `cancer-cell` or `nature-medicine`.
- Phase I/II with strong translational mechanism → `nature-medicine` or `cancer-discovery`.
- Rare haematological malignancy with mechanistic depth → `blood`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet Oncology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does registration / CONSORT / primary endpoint / practice-change scope clear the Lancet Oncology bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / Added-value panel / CONSORT checklist / survival figures / data sharing / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
