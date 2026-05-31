---
name: science-translational-medicine
description: Use when targeting Science Translational Medicine (Sci Transl Med) or deciding whether a translational medicine manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science Translational Medicine (science-translational-medicine)

## Journal positioning

Science Translational Medicine is an AAAS journal occupying the explicit mechanism-to-bedside tier of translational research: every paper must demonstrate both a mechanistic insight and a credible arc toward clinical application — a drug, device, biomarker, or intervention that shows measurable clinical plausibility in human subjects or validated preclinical-to-clinical bridging. This dual mandate distinguishes Sci Transl Med from JCI (which may publish mechanism with human corroboration but without an explicit clinical translation arm) and from Nature Medicine (which requires broader significance but not necessarily a translation demonstration). The readership is translational researchers, physician-scientists, biotech and pharma scientists, and clinical investigators who need both the mechanism and the "so what for the clinic" in the same paper.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAAS / Science Translational Medicine platform.

## When to trigger

- The author names Sci Transl Med or AAAS translational as the target venue.
- A mechanism-plus-clinical-arm paper needs venue selection among Sci Transl Med, JCI, and Nature Medicine.
- A preclinical study with a human proof-of-concept pilot or biomarker validation component needs framing guidance.
- The author needs Sci Transl Med's desk-reject risks and a ranked alternative list before submitting.

## Scope & topic fit

- Disease mechanism studies paired with a human clinical arm: early-phase clinical trial, patient-derived tissue validation, clinical biomarker validation, or pharmacodynamic evidence in a target patient population.
- Drug, biologic, or cell-therapy development studies: target identification, mechanism-of-action validation, and human clinical evidence (PK/PD, biomarker, phase I/II efficacy signal) in one integrated package.
- Medical device, diagnostic, or imaging technology studies where the mechanism of action is established and a human feasibility or validation study demonstrates clinical plausibility.
- Biomarker development and validation studies: discovery in disease samples, mechanistic grounding in biology, and clinical validation with appropriate sensitivity/specificity and clinical utility demonstration.
- Precision medicine and genomics: genomic variant-to-mechanism-to-patient-stratification papers where actionable clinical application is demonstrated, not only inferred.
- Immunotherapy and vaccine mechanism papers with human immune response data or clinical efficacy data in an early-phase trial.

## Method & evidence bar

- Every paper must contain a human component as an integral part of the primary results — not as an optional validation appendix; human clinical samples, patient-derived organoids, early-phase trial data, or clinical biomarker studies are the norm.
- The preclinical (animal or in vitro) data must be validated in a disease-relevant model (PDX, humanized mouse, disease-specific genetic model) before the human arm; healthy-animal toxicology alone is insufficient.
- Clinical translation arm must demonstrate measurable biology in humans: pharmacodynamic target engagement, patient biomarker shift, safety/tolerability with mechanism endpoint, or pilot efficacy signal — not merely "we plan to test this."
- Statistics must be pre-specified for the clinical component; for animal data, ARRIVE checklist compliance; for early-phase trials, CONSORT or equivalent reporting.
- Data and code availability statements required; clinical trial data must be registered; human sample studies require IRB/ethics documentation.
- Reporting guideline checklists must be completed and uploaded at submission.

## Structure & house style

- Sci Transl Med uses a distinctive format: structured Abstract with a specific "Editor's Summary" framing — a short lay-science narrative that bridges mechanism to clinical relevance written for a sophisticated non-specialist. The title itself should be declarative and convey the translational claim.
- The "Translational Relevance" or equivalent summary statement (check current format requirements) must explicitly articulate: what is the disease, what is the mechanism, and what is the clinical take-home — in accessible language.
- Results are organized around the translational arc: (1) mechanistic discovery → (2) preclinical validation in disease-relevant model → (3) human evidence; the paper must flow through this arc, not merely append a human figure at the end.
- Figures: preclinical and clinical data are often interleaved to support the narrative arc; do not relegate all human data to a final supplementary figure.
- Research Articles and Focus articles differ in format; the standard original Research Article has a strict structure — re-check current specifications.
- Extended-data figures or supplementary materials carry supporting data; primary mechanistic and clinical results must remain in the main manuscript.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Science Translational Medicine author instructions" on the AAAS platform and follow the current version.
- Re-check article-type classification (Research Article, Research Letter, Clinical Trial) and confirm current length, figure, and word limits.
- Confirm prospective clinical trial registration (ClinicalTrials.gov or equivalent) for all human study components; upload IRB/ethics and informed-consent documentation.
- Complete and upload the applicable reporting guideline checklist (CONSORT, ARRIVE, STROBE, TRIPOD, or equivalent).
- Verify AAAS conflict-of-interest and funding disclosure requirements; confirm all industry relationships are disclosed.
- Re-check data and code availability statement and requirements for deposition of clinical trial data, sequencing data, or other primary datasets.
- Confirm "Editor's Summary" / translational relevance statement format and current AI-use disclosure policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence capturing the mechanism and the clinical translation arc: what disease, what mechanism, what human evidence, what clinical implication.
- [ ] Human data (clinical samples, trial endpoints, biomarker validation) constitutes an integral primary results component — not a supplementary figure.
- [ ] The preclinical model is disease-relevant (PDX, humanized mouse, patient-derived organoid); healthy-animal pharmacology alone is not sufficient.
- [ ] The title is declarative and translational — it states what was found and why it matters clinically.
- [ ] Trial registration, reporting guideline checklist, ethics/consent, and COI disclosures are complete.
- [ ] The "Editor's Summary" or translational framing statement bridges mechanism to clinical application in accessible language.

## Common desk-reject triggers

- Papers with strong preclinical mechanism but no human clinical component; those belong in `journal-of-clinical-investigation` or disease-specific basic journals.
- Papers where the "human" component is a single patient sample or a retrospective correlation with no mechanistic grounding; one tissue sample does not constitute a clinical translation arm.
- Clinical trials with no mechanistic component; purely clinical efficacy trials belong in `nejm`, `the-lancet`, or disease-specialty clinical journals.
- Missing or vague "translational relevance" statement; AAAS editors triage based on whether the clinical arc is clear and credible in the abstract.
- Reporting guideline checklists absent; clinical trial registration missing; IRB documentation incomplete.

## Re-routing decision

- A pure disease-mechanism paper with strong human corroboration but no clinical translation arm → `journal-of-clinical-investigation` (ASCI; mechanism-of-disease with human relevance, no clinical application required).
- A high-significance translational paper that also demonstrates clinical trial efficacy at practice-changing scale → `nature-medicine` (broader significance required; Nat Med spans mechanism to clinical).
- A cancer translational study with mechanism + human tumor validation → `cancer-discovery` (AACR) if the cancer biology framing is primary.
- An immunotherapy mechanism + early-phase trial paper → `nature-medicine` or `journal-of-clinical-investigation` depending on the depth of mechanism vs. clinical emphasis.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science Translational Medicine
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the mechanism-to-human-evidence arc / disease-relevant preclinical model / clinical arm clear the Sci Transl Med bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Editor's Summary / CONSORT + ARRIVE / trial registration / IRB / COI / data deposition>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
