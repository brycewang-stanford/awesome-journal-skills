---
name: plos-medicine
description: Use when targeting PLOS Medicine or deciding whether a medicine or public-health manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# PLOS Medicine (plos-medicine)

## Journal positioning

PLOS Medicine is an open-access general medical journal published by the Public Library of Science (PLOS). It focuses on research with direct relevance to clinical practice, public health, and health policy, with a strong commitment to global health equity, transparent reporting, and methodological rigour. PLOS Medicine publishes across the full spectrum of medical research, from randomised trials and systematic reviews to health systems analyses and epidemiological studies, provided the work is clinically or public-health relevant and meets strict reporting standards. The journal explicitly refuses to publish industry-sponsored, ghost-authored, or commercially conflicted manuscripts whose independence cannot be established.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the PLOS Medicine site or submission system.

## When to trigger

- The author names PLOS Medicine as a target venue, particularly for open-access clinical or public-health research.
- A well-executed clinical or epidemiological study needs an open-access home and the author values transparency and immediate public access.
- A manuscript addresses health equity, disease burden in LMICs, or global public health in a way that benefits from broad, free dissemination.
- The author is choosing between PLOS Medicine and other open-access or society-journal venues on significance, scope, or cost.

## Scope & topic fit

- Randomised controlled trials and quasi-experimental studies with patient-centred or population-level outcomes across clinical and public-health settings.
- Systematic reviews and meta-analyses addressing clinically or policy-relevant questions across all areas of medicine.
- Prospective and retrospective cohort studies, case-control studies, and cross-sectional analyses with population-level health relevance.
- Health policy analyses, health systems research, and implementation science.
- Global health and disease burden analyses, particularly those addressing low- and middle-income country populations and health equity.
- Research synthesis methods, clinical epidemiology methods, and meta-research (research on research).

## Method & evidence bar

- Randomised trials must be registered, CONSORT-compliant, and clearly distinguish pre-specified from post-hoc analyses.
- Systematic reviews require PRISMA adherence and PROSPERO registration; GRADE ratings of evidence quality are expected for clinical questions.
- All observational studies require STROBE reporting; for diagnostic and prediction studies, STARD and TRIPOD standards apply.
- PLOS Medicine requires a completed and submitted reporting-guideline checklist for every study type; this is a condition of editorial consideration, not a suggestion.
- Data availability is a firm requirement: underlying data must be deposited in a public or managed repository; data requests through author email are not sufficient unless access restrictions are formally justified.
- Competing interests and independence from industry sponsors must be declared in full; manuscripts where the funder controlled data access, analysis, or publication decision are desk-rejected.
- ICMJE authorship, author-contribution statements, ethics approval, and participant-consent documentation are mandatory.

## Structure & house style

- PLOS Medicine articles follow a structured IMRaD format with the heading sequence Title, Abstract, Introduction, Methods, Results, Discussion.
- The structured abstract uses headings Background, Methods and Findings, and Conclusions; it must contain the key quantitative findings and a plain-language interpretation.
- Each manuscript is required to include an "Author Summary"—a short, jargon-free paragraph written for a general audience explaining why the study was done and what the findings mean.
- A "What Do These Findings Mean?" paragraph at the end of the Discussion is a required section and must address clinical, policy, or public-health implications directly.
- PLOS uses a consistent reference style; references are numbered and deposited in a reference management system format.
- Figures must be submitted at publication resolution; data underlying each figure must be deposited or included as supporting information.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "PLOS Medicine submission guidelines" and follow the current PLOS version.
- Re-check current article types, word limits, abstract format, and Author Summary requirements.
- Confirm registration number (trials and reviews), ethics approval reference, and informed-consent statement are in the manuscript.
- Submit the required reporting-guideline checklist (CONSORT/PRISMA/STROBE/STARD/TRIPOD) as a supporting file.
- Confirm the data-availability statement identifies the specific repository and accession or DOI; "available on request" is not acceptable without formal justification.
- Re-check PLOS's competing-interests policy in detail; confirm the funder had no role in study design, data collection, analysis, decision to publish, or manuscript preparation.
- Re-check APC (open-access fee), funding waivers for LMIC authors, and current licensing options (PLOS uses CC BY).
- Re-check AI-use disclosure requirements and preprint policy (PLOS encourages preprints; confirm posting specifics).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the clinical, public-health, or policy implication of the finding, framed for the broadest possible medical audience.
- [ ] The Author Summary is written, is jargon-free, and conveys the study rationale and key finding to a non-specialist.
- [ ] The "What Do These Findings Mean?" section is complete, specific, and not a restatement of the Results.
- [ ] Reporting-guideline checklist is fully completed and ready to upload.
- [ ] Data underlying all figures is deposited in a public repository; accession or DOI is included in the manuscript.
- [ ] Competing-interests declaration covers all authors and all funding sources; independence of analysis from industry funders is documented.

## Common desk-reject triggers

- Reporting-guideline checklist absent or not matching the study type—PLOS conducts a structured screening of every submission.
- Data not deposited or a data-availability statement that relies solely on "data available from the corresponding author on request."
- Industry-funded manuscript where the sponsor controlled data, analysis, or publication; or where authorship conflicts with ICMJE criteria.
- Study lacks a registered protocol (for trials) or PROSPERO record (for systematic reviews) without explanation.
- Author Summary absent or uses highly technical language inappropriate for a general audience.
- "What Do These Findings Mean?" section absent or is a verbatim repetition of the abstract conclusions.

## Re-routing decision

- Higher-significance clinical practice-changing evidence → `the-lancet`, `jama`, or `the-bmj`.
- Strong methodological or EBM contribution → `the-bmj` or `annals-of-internal-medicine`.
- Translational mechanism-to-trial design → `nature-medicine`.
- Basic or open-access life-science focus with broader biology framing → `plos-biology`.
- Oncology-specific clinical findings → `the-lancet-oncology` or `journal-of-clinical-oncology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] PLOS Medicine
[Topic tags] <2–3 closest topics>
[Method/evidence] <does trial registration / CONSORT-PRISMA / open data / independent funding clear the PLOS Medicine bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / Author Summary / reporting checklist / data deposition / competing interests / APC>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
