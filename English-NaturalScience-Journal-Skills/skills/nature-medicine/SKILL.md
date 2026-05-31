---
name: nature-medicine
description: Use when targeting Nature Medicine or deciding whether a translational or clinical medicine manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Medicine (nature-medicine)

## Journal positioning

Nature Medicine, published by Springer Nature, is the premier translational and clinical medicine journal in the Nature family. It publishes research that moves from biological mechanism to clinical application—spanning fundamental disease biology, biomarker discovery, clinical trials, and computational medicine—as long as the work has direct and demonstrated relevance to human disease. The journal demands both biological depth and clinical plausibility; purely preclinical studies without a clear translational bridge, and purely clinical studies without mechanistic insight, each face a steep hurdle. The readership spans translational researchers, physician-scientists, and clinical trialists worldwide.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature site or submission system.

## When to trigger

- The author names Nature Medicine as the target venue for a translational study, first-in-human trial, or biomarker/diagnostic discovery.
- A manuscript moves from a mechanistic finding in human tissue or model systems to a clinical cohort or trial and needs guidance on framing the translational arc.
- A clinical genomics, AI/ML-based diagnostic, or multi-omics disease-subtyping study needs a venue that bridges discovery science and clinical impact.
- The author needs Nature Medicine's desk-reject risks and credible alternatives before submitting.

## Scope & topic fit

- Mechanism-to-clinical translational studies: disease biology in human specimens or validated model systems directly connected to a patient cohort or clinical outcome.
- Biomarker discovery and clinical validation: diagnostic, prognostic, or pharmacodynamic biomarkers validated in independent, adequately powered clinical cohorts.
- First-in-human or proof-of-concept clinical trials with mechanistic readouts (pharmacodynamics, target engagement, correlative biomarkers).
- Computational and AI/ML approaches to diagnosis, prognosis, or treatment selection, validated prospectively or in well-characterised retrospective cohorts with external validation.
- Pandemic and emerging-infectious-disease science that requires both mechanistic understanding and clinical or epidemiological validation.
- Multi-omics disease characterisation (genomics, proteomics, single-cell) that identifies clinically actionable disease subtypes or treatment targets.

## Method & evidence bar

- The translational claim must be supported by convergent evidence: mechanistic data (human tissue, patient-derived models, or rigorously validated preclinical models) plus a clinical validation dataset or trial endpoint.
- Clinical trials must be registered and reported following CONSORT; first-in-human and phase I/II studies are welcome when mechanistic correlatives provide insight beyond safety/efficacy alone.
- Biomarker studies must demonstrate analytical validity and clinical validity; external cohort validation and prospective validation data are expected at the top of the bar.
- AI/ML diagnostic or prognostic tools must be developed and validated on independent cohorts; TRIPOD-AI (or current equivalent) reporting is expected; source code or model weights should be made available.
- Reporting standards: CONSORT for trials, PRISMA for reviews, STROBE for observational components, with appropriate checklist submission.
- Data, code, and materials availability: a Nature-family reporting summary is required; data deposition in an appropriate public repository is expected; code must be accessible.
- ICMJE authorship, author contributions, ethics approval, informed consent, and competing-interests disclosure are mandatory.

## Structure & house style

- Nature Medicine uses a narrative-format manuscript (no rigid IMRaD labelling in the main text for Articles); the story arc should move from biological rationale → translational evidence → clinical implication.
- Abstract is unstructured but must cover rationale, approach, key results, and clinical significance in a paragraph readable by the broad Nature Medicine audience.
- A dedicated Methods section (full detail) is required; extended data figures carry additional results; source data should be deposited for key quantitative figures.
- Nature-family reporting summary (statistics, reproducibility, randomisation, blinding, sample-size justification) must be completed and submitted.
- Life-sciences reporting guidelines apply: blinding of analyses, inclusion of both biological and technical replicates, and an explicit statement of statistical tests and assumptions.
- Figure quality: publication-ready; key mechanistic and clinical data should be in the main figures; flow cytometry, histology, and gel images require full gating/acquisition details in methods.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Medicine author information" and follow the current Springer Nature version.
- Re-check article types (Article vs. Brief Communication vs. Perspective), current length guidelines, and extended-data figure allowances.
- Complete and submit the Nature-family Reporting Summary; confirm all statistical reporting requirements within the summary are addressed.
- Confirm trial registration number, ethics approval, and informed-consent statement.
- Submit CONSORT (trials) or STROBE (observational) or TRIPOD-AI checklist as appropriate.
- Re-check data and code availability requirements: identify the appropriate repository for the data type (e.g., GEO for genomics, dbGaP for controlled-access human data).
- Re-check competing-interests disclosure, funding statement, author-contribution statement, and AI-use disclosure.
- Re-check embargo policy (Nature journals have strict pre-publication embargo rules).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The translational arc is explicit: state the biological mechanism and the clinical validation evidence in the same paper or the same series of experiments.
- [ ] The abstract conveys both mechanistic insight and clinical significance; a clinical trialist and a cell biologist could both find it compelling.
- [ ] A Nature-family Reporting Summary is drafted and addresses all required fields.
- [ ] External validation of biomarker or AI/ML findings is present; single-cohort discovery-only studies are flagged as requiring further validation.
- [ ] Source data are deposited or prepared for deposition; code is accessible in a public repository.
- [ ] Ethics approvals, trial registration, and consent are documented; data-use agreements and patient-privacy protections are described.

## Common desk-reject triggers

- Purely preclinical study without a human-disease connection demonstrated in the paper (not promised for future work).
- Purely clinical trial without mechanistic or biomarker data that adds scientific insight beyond the efficacy/safety result alone.
- Biomarker paper with discovery in one cohort but no independent validation cohort.
- AI/ML tool validated only in the training/test split without an independent external cohort.
- Nature-family Reporting Summary incomplete, or source data unavailable for key quantitative figures.
- Advance is incremental relative to already-published work from the same group or similar studies—novelty is judged harshly against the Nature Medicine significance bar.

## Re-routing decision

- Definitive clinical trial without a mechanistic dimension → `the-lancet`, `jama`, or `nejm`.
- Purely mechanistic disease-biology study → `cancer-cell`, `cell`, or `immunity` depending on the focus.
- Translational but a lower significance bar is more appropriate → `science-translational-medicine` or `journal-of-clinical-investigation`.
- Open-access clinical focus → `plos-medicine`.
- Oncology-specific mechanism-to-trial → `the-lancet-oncology` or `journal-of-clinical-oncology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Medicine
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the translational arc / external validation / Reporting Summary clear Nature Medicine's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / Reporting Summary / trial registration / reporting checklist / data & code deposition / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
