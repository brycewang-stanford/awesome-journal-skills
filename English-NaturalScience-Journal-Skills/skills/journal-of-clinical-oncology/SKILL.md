---
name: journal-of-clinical-oncology
description: Use when targeting Journal of Clinical Oncology (JCO) or deciding whether a clinical oncology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Clinical Oncology (journal-of-clinical-oncology)

## Journal positioning

The Journal of Clinical Oncology is the official journal of the American Society of Clinical Oncology (ASCO) and the highest-impact dedicated oncology journal. It publishes definitive clinical research across all cancer types and all phases of oncology—from prevention and screening through treatment and survivorship—with a primary readership of clinical oncologists, oncology researchers, and clinical trialists worldwide. JCO sets the standard for clinical oncology trial reporting and is the destination for results that define or redefine ASCO clinical-practice guidelines. The competitive bar is high: incremental single-arm studies, retrospective analyses of modest size, or translational studies without clinical grounding are unlikely to succeed without exceptional novelty.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ASCO/JCO site or submission system.

## When to trigger

- The author names JCO as the target venue for a phase III oncology trial, definitive evidence synthesis, or ASCO-guideline-supporting analysis.
- A cancer clinical trial is practice-changing within its disease site and the author is deciding between JCO and The Lancet Oncology.
- A cancer survivorship, quality-of-life, or health-disparities study has primary oncology relevance for practising oncologists.
- The author needs JCO's desk-reject profile and credible alternatives before submitting.

## Scope & topic fit

- Phase III randomised controlled trials defining or changing standard of care in solid tumours and haematological malignancies.
- Biomarker-selected trial designs (including umbrella/basket trials), tumour-agnostic therapy evidence, and precision-oncology trial results.
- Large-scale cancer prevention, screening, and early detection trials with definitive endpoint results.
- Cancer survivorship, quality of life, and symptom management: patient-reported outcomes from well-designed randomised trials.
- Health disparities in cancer outcomes and access to cancer care, particularly in the US and globally.
- ASCO Clinical Practice Guidelines and systematic reviews that support guideline development.

## Method & evidence bar

- Phase III trials must be pre-registered (ClinicalTrials.gov mandatory for US trials; ISRCTN or WHO ICTRP for international), CONSORT-compliant in full, and powered for a pre-specified primary endpoint.
- The primary endpoint must be clinically meaningful; overall survival is the gold standard; progression-free survival or response rates are accepted when supported by evidence that surrogate-primary correlation is established or when OS data are immature—but this must be argued explicitly.
- Systematic reviews and meta-analyses of oncology trials require PRISMA adherence, PROSPERO registration, and GRADE evidence profiling aligned with ASCO guideline methodology.
- Patient-reported outcome studies must use validated instruments and follow the CONSORT-PRO extension.
- Retrospective analyses are considered only when the question cannot be addressed prospectively (e.g., rare tumour types) and when the dataset is sufficiently large and rigorously curated with pre-specified analysis.
- Competing-interests disclosure, especially for industry-sponsored trials, is subject to close editorial scrutiny; sponsor's role in design, data access, and analysis must be stated.

## Structure & house style

- JCO uses a structured abstract with the headings Purpose, Patients and Methods, Results, and Conclusion; this format is mandatory for all original reports.
- The manuscript must include a "Clinical Relevance" statement or its equivalent—articulating specifically what the oncologist should do differently for patients as a result of this study.
- Survival curves must include the number of patients at risk at each time point; median follow-up must be reported.
- Subgroup analyses must be identified as pre-specified or exploratory; forest plots should include interaction p-values.
- Statistical reporting follows standard clinical trial conventions: hazard ratios with 95% CI, response rates with confidence intervals, absolute differences at landmark timepoints.
- JCO publishes multiple article types including Original Reports, Brief Reports, Editorials, and JCO Oncology Practice articles; choose the type suited to study size and scope.

## Official-submission checklist

- Search the live site for "Journal of Clinical Oncology author guidelines" and follow the current ASCO version.
- Re-check article type, word limits for each type, and abstract heading requirements.
- Confirm trial registration number and ethics approval reference are present; confirm data-safety monitoring board statement for phase III trials.
- Submit CONSORT checklist (and CONSORT-PRO if reporting PROs) with page citations as a required file.
- Re-check data-sharing statement; ASCO journals encourage data availability; confirm what, where, when, and under what conditions.
- Re-check competing-interests declaration (all authors), funding and sponsor-independence statement, ICMJE author-contribution statement, and AI-use disclosure.
- Confirm PRISMA + GRADE if submitting a systematic review supporting guideline development.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what practising oncologists should change in their clinical management of a specific patient population based on this study's results.
- [ ] The structured abstract uses the exact JCO headings (Purpose / Patients and Methods / Results / Conclusion) and contains quantitative findings.
- [ ] The primary endpoint is the one registered; any co-primary or secondary endpoint that is emphasised is clearly labelled as such.
- [ ] Survival curves include patients-at-risk tables; median follow-up is stated; subgroup analyses are labelled as pre-specified or exploratory.
- [ ] CONSORT checklist is fully completed and ready to upload.
- [ ] All competing interests, especially industry funding, are declared and the sponsor's role in the study is explicitly described.

## Common desk-reject triggers

- Phase II single-arm study in a common tumour type without a breakthrough efficacy signal or rare-disease justification.
- Primary endpoint switched from the registered endpoint without transparent protocol amendment explanation.
- Survival curves lacking patients-at-risk tables or with follow-up too immature for the primary endpoint to be interpretable.
- Abstract headings not matching the JCO required format; "Clinical Relevance" statement absent or vague.
- Retrospective analysis of a commercially available dataset without pre-specified hypotheses or unique analytical value.
- Competing-interests disclosure incomplete or inconsistent with prior public disclosure by authors at conferences.

## Re-routing decision

- Practice-changing trial with global-health or policy scope → `the-lancet-oncology`.
- Early-phase translational trial with mechanistic depth → `nature-medicine` or `cancer-discovery`.
- Haematological malignancy with mechanistic biology → `blood`.
- Cancer biology mechanism without clinical trial data → `cancer-cell`.
- Oncology health-disparities or public-health focus → `plos-medicine` or `the-lancet`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Clinical Oncology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does registration / CONSORT / primary endpoint / clinical-relevance framing clear the JCO bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract headings / CONSORT checklist / survival figures / data sharing / competing interests>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
