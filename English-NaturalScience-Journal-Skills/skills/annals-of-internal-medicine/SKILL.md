---
name: annals-of-internal-medicine
description: Use when targeting Annals of Internal Medicine (Ann Intern Med) or deciding whether an internal medicine or clinical-evidence manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Annals of Internal Medicine (annals-of-internal-medicine)

## Journal positioning

Annals of Internal Medicine is the official journal of the American College of Physicians (ACP), one of the most influential specialty society journals in clinical medicine. It publishes original research, systematic reviews, clinical guidelines, and evidence syntheses directly relevant to adult internal medicine and its subspecialties. The journal prizes rigour, reproducibility, and clinical applicability; it has a strong tradition of methodology papers, including the development and promulgation of reporting guidelines. The readership is internists, general internists, and subspecialists in the US and internationally who require evidence at the point of clinical decision-making.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACP/Annals site or submission system.

## When to trigger

- The author names Annals of Internal Medicine as the target venue for a clinical trial, systematic review, or guideline-supporting analysis in internal medicine or its subspecialties.
- A manuscript addresses a clinical question where evidence quality, reproducibility, or a formal evidence-synthesis methodology is central to the contribution.
- A manuscript proposes or validates a new reporting guideline, clinical prediction rule, or diagnostic-accuracy tool applicable to adult internal medicine.
- The author needs Annals' desk-reject profile and credible alternatives before submitting.

## Scope & topic fit

- Randomised controlled trials and observational studies addressing clinical questions in adult internal medicine, including cardiovascular disease, diabetes, infectious disease, oncology (general medicine aspects), pulmonology, gastroenterology, and geriatrics.
- Systematic reviews and meta-analyses that synthesise evidence to inform clinical practice guidelines; reviews that apply GRADE methodology and produce actionable evidence summaries.
- Clinical-guideline papers, evidence-based clinical-practice recommendations, and ACP guideline statements.
- Diagnostic-accuracy and clinical-prediction-model studies (STARD, TRIPOD) for conditions relevant to internists.
- Research on research methodology—reproducibility, reporting-guideline development and validation, research synthesis methods.
- Health-services research on quality of care, value, and outcomes within adult medicine populations.

## Method & evidence bar

- Clinical trials must be pre-registered, CONSORT-compliant, and powered for clinically meaningful primary outcomes; surrogate-endpoint-only trials with no patient-centred secondary outcomes are unlikely to meet the bar.
- Systematic reviews require PRISMA adherence and PROSPERO registration; GRADE evidence profiling is standard; the review must address a focused, clinically answerable question with a pre-specified protocol.
- Observational studies require STROBE adherence; Annals expects a discussion of potential for unmeasured confounding with quantitative bias analysis or sensitivity analyses where feasible.
- A reproducible-research statement is expected: authors should describe steps taken to ensure analysis reproducibility, including pre-registered analysis plans, code or algorithm availability, and data-availability details.
- Diagnostic studies must follow STARD; prediction models must follow TRIPOD; both require prospective or well-characterised validation cohorts.
- ICMJE authorship criteria and author-contribution statements are required; Annals scrutinises ghost-authorship and industry influence carefully.

## Structure & house style

- Annals uses a structured abstract for original research (background, objective, design, setting, participants, measurements, results, limitation, conclusion) with a mandatory Limitation paragraph; omitting the limitation from the abstract is a formatting error.
- A "Primary Funding Source" line is required at the end of the abstract.
- The manuscript should distinguish the ACP context: results are often cast in terms of what clinicians should recommend to patients today.
- Annals publishes an "In the Clinic" section (largely commissioned reviews), "Ideas and Opinions," and "On Being a Doctor" essays alongside Original Research.
- Tables should summarise the most important results; extensive secondary analyses belong in supplementary appendices.
- Statistical reporting: report confidence intervals and absolute differences; regression results should include both adjusted and unadjusted estimates where interpretable.

## Official-submission checklist

- Search the live site for "Annals of Internal Medicine instructions for authors" and follow the current ACP version.
- Re-check article type (Original Research, Systematic Review, Brief Communication, etc.) and current word/abstract limits.
- Confirm clinical-trial or review registration number, ethics approval, and informed-consent statement in the manuscript.
- Submit the appropriate reporting-guideline checklist (CONSORT/PRISMA/STROBE/STARD/TRIPOD/GRADE summary) with page-number citations.
- Confirm the reproducible-research statement is present; state specifically what data, code, or supplementary materials are available and where.
- Re-check competing-interests disclosure (all authors), funding disclosure, ICMJE author-contribution statement, and AI-use disclosure.
- Re-check the mandatory Limitation paragraph in the abstract and the Primary Funding Source line.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what clinicians in adult internal medicine should do differently because of this study.
- [ ] The structured abstract includes a dedicated Limitation paragraph and a Primary Funding Source line.
- [ ] The primary outcome is the one registered and pre-specified; secondary and sensitivity analyses are labelled as such.
- [ ] Reporting-guideline checklist is complete with page-number citations ready to upload.
- [ ] A reproducible-research or data-availability statement is explicit about what is shared and how to access it.
- [ ] All competing interests and funding sources are disclosed; author contributions meet ICMJE criteria.

## Common desk-reject triggers

- Structured abstract missing the Limitation paragraph or the Primary Funding Source line—a formal formatting failure checked before peer review.
- Clinical trial not registered, or primary outcome in the manuscript differs from the registered outcome without transparent explanation.
- Systematic review without PROSPERO registration, or meta-analysis based predominantly on high-risk-of-bias studies without GRADE downgrading.
- Scope outside adult internal medicine—paediatric-only or highly specialised surgical studies without clear generalisability to internists.
- Observational study with a large number of comparisons and no pre-specified analysis plan, suggesting post-hoc outcome selection.
- Industry-sponsored manuscript where the funder controlled data access or statistical analysis.

## Re-routing decision

- Practice-changing and global in scope → `the-lancet`; US clinical and broader significance → `jama`.
- ACP guideline content but framed more as health-policy analysis → `the-bmj` or `jama`.
- Strong translational or mechanistic dimension alongside clinical findings → `nature-medicine`.
- Open-access, international public-health emphasis → `plos-medicine`.
- Speciality-specific clinical oncology, infectious disease, or neurology focus → `journal-of-clinical-oncology`, `the-lancet-infectious-diseases`, or `the-lancet-neurology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Annals of Internal Medicine
[Topic tags] <2–3 closest topics>
[Method/evidence] <does registration / CONSORT-PRISMA / GRADE / reproducible-research statement clear the Annals bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / abstract Limitation paragraph / reporting checklist / reproducibility statement / data sharing / competing interests>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
