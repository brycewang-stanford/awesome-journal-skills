---
name: the-lancet-neurology
description: Use when targeting The Lancet Neurology or deciding whether a clinical neurology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Lancet Neurology (the-lancet-neurology)

## Journal positioning

The Lancet Neurology is the leading specialty journal in the Lancet family focused on clinical neurology and neuroscience with clinical relevance, published by Elsevier. It publishes practice-changing neurological trials, major epidemiological studies on neurological disease burden, translational advances directly linked to clinical neurology, and policy analyses for neurological disease control. The editorial culture mirrors the Lancet parent: rigorous trial registration, CONSORT compliance, a global-health and equity lens, and an insistence that findings shift neurological practice or policy at scale. Purely mechanistic neuroscience or animal-model studies without a compelling clinical bridge are out of scope; equally, confirmatory or incremental clinical studies that do not alter existing practice will not meet the bar.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Lancet/Elsevier site or submission system.

## When to trigger

- The author names The Lancet Neurology as the target venue for a neurological clinical trial, disease-burden analysis, or translational neurology study.
- A phase III trial in stroke, multiple sclerosis, Parkinson's disease, epilepsy, dementia, neuro-oncology, or another major neurological disease has results that change standard of care.
- A neurological disease-burden analysis or neuroepidemiology study has global-health policy implications and is ready for high-impact specialty publication.
- The author needs The Lancet Neurology's desk-reject risks and credible alternatives before submitting.

## Scope & topic fit

- Phase III and large phase II randomised controlled trials in major neurological conditions: stroke and cerebrovascular disease, multiple sclerosis, dementia and Alzheimer's disease, Parkinson's disease, epilepsy, headache and migraine, rare neurological diseases.
- Biomarker-defined patient populations in neurological trials: CSF, imaging, or blood biomarkers (including plasma p-tau, neurofilament light chain) used as stratification or primary-endpoint components in clinical trials.
- Neuroepidemiology and global neurological disease burden: incidence, prevalence, disability-adjusted life years, and risk factor epidemiology with policy implications.
- Precision neurology: genetic, proteomic, or imaging-based disease subtyping with direct management implications in a clinical trial context.
- Neurorehabilitation and neurological disability: well-powered trials with patient-centred functional outcomes.
- Translational neurology: mechanism-to-trial studies where neurobiological insight drives the clinical intervention and is tested in a clinical cohort.

## Method & evidence bar

- Randomised trials must be pre-registered, CONSORT-compliant in full, and powered for clinically meaningful primary endpoints; functional independence scales, cognitive battery outcomes, and patient-reported outcomes are standard primary endpoints for neurological trials and must be validated.
- Neuroimaging studies as primary evidence require pre-specified acquisition protocols, quantitative analysis pipelines, and, for multisite studies, harmonisation documentation.
- Biomarker studies embedded within trials must report diagnostic accuracy (sensitivity, specificity, AUC) for the proposed clinical decision threshold; longitudinal biomarker trajectories require adequate follow-up and mixed-effects modelling.
- Epidemiological studies require STROBE adherence; global burden analyses should align with GBD or equivalent methodology and present DALYS/YLDs in addition to incidence/prevalence.
- Systematic reviews of neurological trials require PRISMA, PROSPERO registration, and GRADE evidence grading; network meta-analyses are welcomed when they resolve comparative effectiveness questions.
- Ethics, informed consent, and ICMJE authorship are mandatory; data sharing for trial IPD is strongly encouraged.

## Structure & house style

- The Lancet Neurology uses the Lancet family structured abstract (background, methods, findings, interpretation) with a mandatory funding statement.
- An "Added value of this study" panel (what is already known, what this study adds) is required; the panel must identify the specific evidence gap—not a general statement that the topic is important.
- Opening paragraphs must frame the unmet clinical need, the current standard of care in neurology, and the population-level burden that motivates the study.
- Survival or time-to-event analyses in neurological trials (e.g., time to relapse, time to disability worsening) must include Kaplan-Meier curves with patients-at-risk tables and hazard ratios with confidence intervals.
- Neuroimaging figures should be high resolution and include representative cases plus quantitative group-level data; captions must include acquisition parameters where critical.
- Subgroup analyses must be declared as pre-specified or exploratory; interaction p-values are expected in forest plots.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The Lancet Neurology information for authors" and follow the current Elsevier/Lancet version.
- Re-check article type, current word and figure limits, and "Added value" panel format.
- Confirm trial registration number, ethics approval reference, and informed-consent statement in the manuscript.
- Submit CONSORT checklist (or PRISMA for reviews, or STROBE for observational studies) with page-number citations.
- Re-check data-sharing statement; for trials, specify what IPD will be shared, via which repository, and under what access conditions.
- Re-check competing-interests declaration, funding disclosure, ICMJE author-contribution statement, and AI-use disclosure.
- Re-check open-access/APC, licensing, and preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating which current standard of neurological care this study changes, and for which patient population and disease stage.
- [ ] The CONSORT flow diagram is prepared; Kaplan-Meier curves include patients-at-risk tables; hazard ratios and absolute outcome rates are reported.
- [ ] The "Added value" panel identifies the specific evidence gap (not generic importance) and what is now established by this study.
- [ ] Biomarker analyses are labelled as pre-specified (for primary/secondary endpoints) or exploratory (for hypothesis-generating correlatives).
- [ ] Trial registration, ethics, and data-sharing statement are complete and self-consistent.
- [ ] Neuroimaging or biomarker methodologies are described in sufficient detail for reproducibility; multisite harmonisation is documented.

## Common desk-reject triggers

- Phase II or small phase III trial with a surrogate imaging endpoint and no patient-centred functional or survival outcome.
- Primary endpoint switched from the registered endpoint without a protocol-amendment explanation.
- CONSORT non-compliance; "Added value" panel absent or generic.
- Neuroimaging study presented as practice-changing without clinical trial validation; proof-of-concept imaging biomarkers without a companion clinical cohort.
- Epidemiological study limited to a single country or region without addressing how findings extend to the global neurological disease burden.
- Translational neuroscience study with animal or in vitro data only and no human clinical data in the same paper.

## Re-routing decision

- Neurological findings with pan-medicine or health-policy scope → `the-lancet`.
- Mechanistic neuroscience without clinical trial evidence → `neuron` or `nature-neuroscience`.
- Translational mechanism-to-trial with broad medical significance → `nature-medicine`.
- Biological psychiatry or psychiatric neuroscience → `molecular-psychiatry`.
- Neuro-oncology trial with strong oncology framing → `the-lancet-oncology` or `journal-of-clinical-oncology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet Neurology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does registration / CONSORT / patient-centred endpoint / global burden framing clear the journal's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / Added-value panel / CONSORT checklist / survival figures / data sharing / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
