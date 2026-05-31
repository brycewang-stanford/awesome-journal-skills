---
name: the-bmj
description: Use when targeting The BMJ or deciding whether a clinical medicine or evidence-based medicine manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The BMJ (the-bmj)

## Journal positioning

The BMJ (British Medical Journal), published by the BMJ Publishing Group, is one of the world's leading general medical journals with a distinctive patient-centred, evidence-based medicine (EBM) identity. The BMJ prizes methodological transparency, open data, patient and public involvement in research, and research integrity; it has taken editorial positions on over-medicalisation, research waste, and the need for real-world evidence. The readership is global—clinicians, researchers, educators, and policymakers—with a particularly strong UK and Commonwealth presence, though the editorial bar applies internationally.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the BMJ's own site or submission system.

## When to trigger

- The author names The BMJ as the target venue for a clinical trial, systematic review, observational study, or analysis methodology paper.
- A manuscript has strong methodological novelty, open-data commitments, or a patient/public-involvement narrative that The BMJ's culture explicitly rewards.
- A paper critiques evidence quality, clinical guidelines, or research methodology at a level that fits The BMJ's commentary and analysis tradition.
- The author needs The BMJ's specific desk-reject risks and alternatives before submitting.

## Scope & topic fit

- Randomised controlled trials with patient-centred outcomes, including pragmatic and platform trials, particularly those addressing real-world clinical settings.
- Systematic reviews and meta-analyses, especially those applying novel methodology (network meta-analysis, individual participant data) or resolving long-contested questions.
- Large observational studies using routinely collected health data (electronic health records, administrative data) with robust causal methods.
- Clinical epidemiology methods papers: new statistical approaches, bias assessment methods, prediction-model reporting and validation.
- Patient and public involvement (PPI) in research design, conduct, and reporting—The BMJ actively commissions and credits PPI contributions.
- Analyses of healthcare quality, safety, research waste, reproducibility, and publication bias.

## Method & evidence bar

- Randomised trials must be registered, CONSORT-compliant, and include a patient or public-involvement statement describing how patients contributed to design, conduct, or dissemination.
- Systematic reviews require PRISMA adherence and PROSPERO registration; GRADE evidence profiling is expected; the review must add genuine synthesis beyond what existing reviews provide.
- Observational studies must follow STROBE; methods to address confounding (propensity score, instrumental variable, negative control, E-value) should be used and reported explicitly.
- Open data is a strong editorial value: individual participant data sharing is encouraged for trials; data-availability statements must specify what is shared, where deposited, and under what conditions.
- Statistical reporting standard: absolute effects, confidence intervals, NNT/NNH for trials; no sole reliance on p-values; adherence to the current CONSORT extension for the specific trial type (cluster, crossover, factorial, etc.).
- Competing-interests disclosure and sponsor independence are scrutinised carefully; industry-funded studies must demonstrate statistical independence and full data access for authors.

## Structure & house style

- The BMJ uses a structured abstract (objective, design, setting, participants, main outcome measures, results, conclusions); a "What is already known on this topic / What this study adds" box is required and must be genuinely specific.
- The introduction is concise and anchored in the clinical or public-health problem; state the objective in the final sentence of the introduction.
- The BMJ's Research article format runs shorter than some competitors; prioritise clarity over completeness and move secondary analyses to supplementary material.
- Patient and public involvement must be reported in a dedicated section; describe who was involved, how, and what changed as a result.
- Plain-language summary or lay abstract is expected and given editorial weight.
- Figures should carry their own explanatory legends; data visualisation is valued; tables should not replicate figure content.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The BMJ instructions for authors" and follow the current BMJ Publishing Group version.
- Re-check article type and current word and abstract limits; confirm the "What is already known / What this study adds" box requirements.
- Confirm trial or review registration number and ethics approval reference are stated in the methods.
- Submit the appropriate reporting-guideline checklist (CONSORT/PRISMA/STROBE/TRIPOD/STARD) as required.
- Re-check data-sharing statement requirements and any repository deposition expectations.
- Re-check the patient and public involvement reporting requirements in the current author instructions.
- Confirm competing-interests declaration (all authors and patient contributors), funding and sponsor-independence statement, author contributions (ICMJE), and AI-use disclosure.
- Re-check open-access/APC, licensing (BMJ has specific OA routes), and preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this finding or method matters to clinicians, patients, or health systems—framed from the patient's perspective where possible.
- [ ] The contribution is stated as new evidence, methodological advance, or evidence synthesis—not as "the first study ever to examine."
- [ ] The "What is already known / What this study adds" box is specific and not a vague summary of the abstract.
- [ ] Patient and public involvement section is completed; if no PPI occurred, explain why and what the limitation implies.
- [ ] Reporting-guideline checklist is ready; open-data or data-availability statement is complete.
- [ ] All financial and non-financial competing interests are declared; sponsor independence in analysis and publication is documented.

## Common desk-reject triggers

- No patient and public involvement statement, or a boilerplate statement that does not describe actual involvement.
- CONSORT or PRISMA checklist missing; trial registration absent or registration number not cited in the methods.
- Data-sharing statement absent or vague—stating "data available on reasonable request" without details increasingly fails the bar.
- Industry-sponsored study where authors lacked independent access to the full dataset or where statistical analysis was conducted solely by the sponsor.
- "What this study adds" box that is generic and does not distinguish the study's specific contribution.
- Observational study presented as causal without addressing confounding with appropriate methods or transparency.

## Re-routing decision

- Strong global-health or policy-change emphasis, especially for LMICs → `the-lancet`.
- Structured-abstract AMA style and US clinical-practice framing → `jama`.
- ACP internal-medicine focus with guideline implications → `annals-of-internal-medicine`.
- Translational or mechanistic dimension alongside clinical findings → `nature-medicine`.
- Open-access general medicine with strong public-health focus → `plos-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The BMJ
[Topic tags] <2–3 closest topics>
[Method/evidence] <does open data / patient involvement / CONSORT-PRISMA compliance clear The BMJ's EBM bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / PPI section / reporting checklist / data sharing / competing interests>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
