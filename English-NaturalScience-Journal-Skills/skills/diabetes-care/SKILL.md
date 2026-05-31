---
name: diabetes-care
description: Use when targeting Diabetes Care (ADA) or deciding whether a diabetes/endocrinology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Diabetes Care (diabetes-care)

## Journal positioning

Diabetes Care is the clinical flagship of the American Diabetes Association and the highest-impact clinical diabetes journal worldwide. Its editorial identity is firmly clinical and translational — randomized trials, epidemiology, clinical care delivery, and applied translational research in type 1 and type 2 diabetes, obesity, and related metabolic conditions — with an explicit emphasis on evidence that can change diabetes clinical practice or ADA Standards of Care. Unlike broader endocrinology journals, Diabetes Care does not publish basic molecular-biology studies without direct clinical application, and unlike general medical journals, it does not demand the single global significance of NEJM or JAMA. The readership is the ADA membership: diabetologists, endocrinologists, diabetes educators, and clinical researchers in cardiometabolic disease.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ADA / Diabetes Care platform.

## When to trigger

- The author names Diabetes Care or the ADA as the target venue for a diabetes or metabolic disease manuscript.
- A diabetes RCT, observational cohort, or technology study needs venue selection between Diabetes Care, Diabetologia, and broader medical journals.
- A paper directly relevant to ADA Standards of Care or clinical diabetes management guidelines needs framing guidance.
- The author needs Diabetes Care's desk-reject risks and alternative venues before submitting.

## Scope & topic fit

- Randomized clinical trials evaluating glucose-lowering therapies, insulin delivery technologies, lifestyle interventions, or complication-prevention strategies in type 1 or type 2 diabetes or prediabetes.
- Cardiovascular outcomes trials (CVOTs) and cardiorenal protection studies in diabetes cohorts where the primary endpoint has ADA clinical-care implications.
- Epidemiology of diabetes incidence, prevalence, complications (retinopathy, nephropathy, neuropathy, cardiovascular), and disparities at population or national scale.
- Diabetes technology and innovation: continuous glucose monitoring, closed-loop/automated insulin delivery, diabetes self-management platforms — with rigorous clinical validation in appropriately powered trials.
- Applied translational research: studies of islet biology, beta-cell function, insulin resistance mechanisms, or adipose/liver metabolism where the primary evidence layer is human samples, genetic data, or validated clinical biomarkers.
- Diabetes care delivery, patient-centered outcomes, health equity, and access-to-care research at a scale and rigor consistent with ADA clinical priority.

## Method & evidence bar

- RCTs must be prospectively registered, CONSORT-compliant, and powered for a pre-specified primary endpoint with clinical diabetes relevance; glycemic endpoints (HbA1c, TIR), cardiovascular outcomes, or complication endpoints are typical primary measures.
- Observational and epidemiologic studies must employ validated diabetes and complication definitions (consistent with ADA diagnostic criteria), pre-specified analysis plans, appropriate confounding control, and explicit limitation discussion.
- Technology evaluation studies (CGM, closed-loop systems) require randomized or rigorously controlled designs with pre-specified glycemic and safety endpoints; real-world registry analyses must address selection bias explicitly.
- Translational studies using human pancreatic tissue, islets, or metabolic phenotyping data must include appropriate human-cohort validation; mechanistic animal studies without human data will not meet the bar for original research (may fit Perspectives or Brief Communications).
- Prediction models must follow TRIPOD standards with external validation; ADA Standards of Care context must be explicit.
- Reporting guideline checklists (CONSORT, STROBE, PRISMA, TRIPOD) must be uploaded at submission.

## Structure & house style

- Structured abstract (Objective / Research Design and Methods / Results / Conclusions) with quantitative results including confidence intervals in Conclusions — this is a firm ADA/Diabetes Care expectation.
- The introduction must frame the gap relative to the current ADA Standards of Care or clinical diabetes landscape; "no study has examined" without connection to clinical practice is insufficient.
- Articles vs. Brief Reports vs. Diabetes Care Perspectives carry different length and format norms — confirm the appropriate article type before submission; the Brief Report format does not accommodate complex multi-endpoint trials.
- Tables should present clinical characteristics, primary and secondary endpoint results with effect sizes and CIs, and subgroup analyses following standard RCT or cohort reporting.
- Supplementary material: protocol, pre-specified statistical analysis plan, and secondary endpoint tables go in the supplement; core results must be in the main text.
- "In a nutshell" or clinical implications callout (check current format) summarizes the take-home message for the clinician reader.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Diabetes Care author instructions" on the ADA / Diabetes Care platform and follow the current version.
- Re-check article-type classification (Original Research, Brief Report, Perspectives in Care, Research Letter) and confirm current length and figure limits.
- Confirm prospective trial registration (ClinicalTrials.gov or equivalent) and upload ethics/IRB and patient-consent documentation.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, TRIPOD, or equivalent).
- Verify ADA conflict-of-interest and funding disclosure requirements; pharmaceutical and device industry relationships must be explicitly disclosed for all authors.
- Re-check data and code availability statement and any requirements for deposition of participant-level data.
- Confirm current AI-use disclosure policy and open-access options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this finding changes or informs ADA clinical diabetes care, Standards of Care, or population-level diabetes management.
- [ ] The structured abstract Conclusions contain quantitative effect sizes with confidence intervals — not just directional language.
- [ ] The applicable reporting guideline checklist is complete; trial registration and ethics/consent documentation are ready for upload.
- [ ] Human clinical data, patient samples, or genetic evidence constitute the primary evidence layer; any mechanistic animal data is clearly framed as supporting rather than primary.
- [ ] The article type is appropriate for the scope and complexity; a large multi-endpoint RCT requires an Original Research article, not a Brief Report.
- [ ] ADA and industry COI disclosures are complete for all authors; no undisclosed industry funding.

## Common desk-reject triggers

- Basic or mechanistic studies (animal models, cell lines) without human clinical validation or an explicit ADA clinical-practice relevance demonstrated in the primary data.
- Glycemic or metabolic studies that use non-ADA-aligned diabetes definitions or diagnostic thresholds without explicit justification.
- Small exploratory pilot studies or underpowered trials presented as definitive; non-pre-specified or retrospective primary endpoints.
- Technology studies lacking a randomized or rigorously controlled design; real-world CGM or device data without pre-specified hypotheses.
- Missing structured abstract or absent quantitative results in the Conclusions — a frequent reason for immediate return.

## Re-routing decision

- A major diabetes CVOT or cardiorenal outcomes trial with field-defining significance → `nejm`, `the-lancet`, or `jama` if the global significance warrants that level.
- A diabetes mechanism or metabolic biology study with strong translational science and limited clinical trial data → `cell-metabolism` (Cell Press; metabolism mechanism in vivo) or `journal-of-clinical-investigation`.
- A clinical endocrinology study spanning beyond diabetes (thyroid, adrenal, reproductive endocrinology) → Journal of Clinical Endocrinology & Metabolism or Endocrinology.
- An obesity pharmacotherapy trial with primary obesity endpoints → Obesity (The Obesity Society) or `nejm` if landmark-scale.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Diabetes Care
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the ADA Standards of Care framing / structured abstract / CONSORT registration clear the Diabetes Care bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / structured abstract / CONSORT or equivalent / trial registration / ADA COI / data availability>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
