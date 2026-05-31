---
name: jama
description: Use when targeting JAMA (Journal of the American Medical Association) or deciding whether a clinical medicine manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# JAMA (jama)

## Journal positioning

JAMA is the flagship journal of the American Medical Association and one of the most widely read peer-reviewed medical journals in the world. It publishes clinically actionable research—particularly randomised trials, systematic reviews, and guideline-informing observational studies—with strict adherence to reporting standards and methodological transparency. The readership is primarily clinicians in practice and clinical researchers; findings must translate directly into patient-care decisions in the US healthcare context and beyond.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AMA/JAMA site or submission system.

## When to trigger

- The author names JAMA as the target venue for a clinical trial, observational study, or systematic review.
- A clinically actionable manuscript needs guidance on JAMA's specific structured-abstract format, reporting-guideline requirements, and editorial culture versus The Lancet or NEJM.
- A general medicine manuscript needs to assess whether its significance and methods meet JAMA's bar.
- The author needs JAMA's desk-reject profile and credible alternatives before submitting.

## Scope & topic fit

- Randomised controlled trials with patient-centred outcomes across internal medicine, surgery, psychiatry, paediatrics, public health, and primary care.
- Large prospective cohort studies or registry analyses with sufficient precision and clinical relevance to inform practice.
- Systematic reviews and meta-analyses of sufficient completeness to serve as a definitive evidence synthesis for clinicians.
- Diagnostic-test accuracy studies and clinical decision-rule derivation and validation studies.
- Health policy, health economics, and comparative effectiveness research directly relevant to US and international clinical practice.
- US healthcare system analyses (utilisation, disparities, quality, outcomes) with generalisable implications.

## Method & evidence bar

- Randomised trials must be prospectively registered (ClinicalTrials.gov or equivalent), CONSORT-compliant in full, and must report the primary outcome as pre-specified; post-hoc re-labelling of outcomes is grounds for rejection.
- Systematic reviews require PRISMA adherence; PROSPERO registration is strongly expected; risk-of-bias assessment and GRADE rating of evidence are expected.
- Observational studies require STROBE adherence, pre-specified analysis plan where feasible, and thorough confounding control with explicit statement of residual confounding.
- JAMA applies strict reporting-guideline compliance: authors must submit the relevant guideline checklist (CONSORT, PRISMA, STROBE, STARD, or TRIPOD) as a required file.
- Ethics approval and informed consent are mandatory; ICMJE authorship criteria must be met with author contributions stated.
- Statistical reporting must include absolute risk differences and confidence intervals alongside relative measures; numbers needed to treat/harm are expected for trial results.

## Structure & house style

- JAMA requires a structured abstract with the headings Importance, Objective, Design/Setting/Participants, Intervention/Exposures, Main Outcomes and Measures, Results, and Conclusions and Relevance; this format is a hard requirement, not a style preference.
- An "Importance" section opens the abstract and must state clinical relevance in one to two sentences for a practising clinician.
- The Key Points section (Question, Findings, Meaning) is mandatory and must be concise and lay-readable; this appears prominently in the published article.
- The manuscript introduction is brief and direct: state the clinical problem, the evidence gap, and the study objective within a few paragraphs.
- JAMA distinguishes article types: Original Investigation, Research Letter, Viewpoint, and others—choose and format accordingly; re-check current type-specific word and table/figure limits.
- AMA style applies to references, units, and statistical notation.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "JAMA instructions for authors" and follow the current AMA version.
- Re-check article type, current word count, abstract heading requirements, and the Key Points format.
- Confirm registration number (for trials and reviews), ethics approval, and informed-consent statement.
- Submit the appropriate reporting-guideline checklist (CONSORT/PRISMA/STROBE/STARD/TRIPOD) as a required file.
- Re-check competing-interests disclosure (all authors), funding source disclosure, author-contribution statement per ICMJE, and AI-use disclosure.
- Re-check data-sharing policy: a data-sharing statement for clinical trials is required; confirm what data will be made available, when, and how.
- Re-check preprint policy and open-access/APC options if applicable.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the clinical action or practice change a practising physician should take based on this study.
- [ ] The structured abstract is complete with all required JAMA headings; the Key Points section (Question / Findings / Meaning) is drafted.
- [ ] The primary outcome is the one registered and pre-specified; secondary and post-hoc analyses are clearly labelled as such.
- [ ] The relevant reporting-guideline checklist is filled out and ready to upload.
- [ ] All authors meet ICMJE criteria; contributions, funding, and competing interests are disclosed.
- [ ] Absolute risk differences (not only relative risks or ORs) are reported for the primary outcome.

## Common desk-reject triggers

- Structured abstract headings missing or using non-JAMA headings; Key Points section absent or not clinician-facing.
- Trials not pre-registered or with primary outcome switched from the registered version without transparent declaration.
- CONSORT, PRISMA, or STROBE checklist not submitted; reporting-guideline non-compliance identified during initial screening.
- Studies powered only for surrogate endpoints without patient-centred outcome data.
- Single-centre, small-sample studies that lack generalisability to clinical practice.
- Industry-sponsored trials with undisclosed conflicts or ghost-authored manuscripts.

## Re-routing decision

- Definitively practice-changing but framed around global health, equity, or policy → `the-lancet` or for US-specific policy depth `annals-of-internal-medicine`.
- Same rigour but a specialty focus (oncology, cardiology, neurology) → consider `journal-of-clinical-oncology`, `circulation`, or a relevant Lancet specialty title.
- Strong EBM emphasis, open data, and patient/public involvement → `the-bmj`.
- Translational science bridging mechanism to clinical trial → `nature-medicine`.
- Lower significance bar but rigorous reporting, open access → `plos-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA
[Topic tags] <2–3 closest topics>
[Method/evidence] <does trial registration / structured abstract / CONSORT compliance clear JAMA's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / structured abstract & Key Points / reporting checklist / data sharing / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
