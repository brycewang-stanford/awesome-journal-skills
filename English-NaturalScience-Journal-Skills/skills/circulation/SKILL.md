---
name: circulation
description: Use when targeting Circulation (AHA) or deciding whether a cardiovascular manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Circulation (circulation)

## Journal positioning

Circulation is the flagship journal of the American Heart Association and the premier general-cardiology venue in North America. It publishes practice-changing clinical trials, mechanistic and translational cardiovascular science, AHA scientific statements, and population-based epidemiology — all judged against whether the result can shift AHA guidelines or reshape cardiovascular clinical thinking at a broad readership of clinicians, clinical investigators, and cardiovascular scientists. The AHA identity means papers must speak to both bench and bedside; a pure-mechanism paper with no translational bridge, or a minor clinical audit, will not clear the bar.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AHA / Circulation publisher site and submission system.

## When to trigger

- The author names Circulation or the AHA as the target venue for a cardiovascular manuscript.
- A cardiovascular RCT, mechanistic study, or epidemiologic cohort paper needs venue selection among Circulation, JACC, or EHJ.
- A manuscript covering an AHA priority area (heart failure, arrhythmia, atherosclerosis, stroke, resuscitation) requires framing guidance.
- The author needs Circulation's specific desk-reject risks and a ranked alternative list before submitting.

## Scope & topic fit

- Large-scale randomized controlled trials in cardiovascular medicine with direct implications for AHA guidelines or clinical standards of care.
- Mechanistic cardiovascular science (cardiac remodeling, vascular biology, arrhythmia mechanisms, heart failure pathophysiology) with clear translational relevance to human disease.
- AHA scientific statements, clinical practice updates, and policy documents (these are typically invited or pre-approved concept submissions).
- Population-level cardiovascular epidemiology, risk-factor science, and prevention research at national or international scale.
- Novel cardiovascular imaging, biomarker, or device studies where the clinical impact is definitive, not exploratory.

## Method & evidence bar

- RCTs must be prospectively registered, CONSORT-compliant, and powered for a clinically meaningful primary endpoint; protocol and analysis plan disclosed.
- Observational and epidemiologic studies require pre-specified exposure/outcome definitions, rigorous confounding control (matching, multivariable, or propensity approaches), and explicit limitation discussion.
- Mechanistic studies (in vitro, animal, or translational) must include human-relevance validation; a rodent-only study without a human data bridge will not meet the bar.
- Biomarker or diagnostic studies should follow TRIPOD or equivalent reporting standards and demonstrate incremental clinical utility (e.g., net reclassification, C-statistic improvement) beyond standard measures.
- Statistical methodology must reflect current cardiovascular-trial standards; Bayesian trials, adaptive designs, and platform trials are welcome but must follow current reporting guidance.
- Data and code availability statements are expected; pre-registration of observational analyses is encouraged.

## Structure & house style

- Original research uses a structured abstract (Background / Methods / Results / Conclusions); the Results and Conclusions must contain quantitative effect sizes with confidence intervals.
- The introduction should frame the gap relative to the current AHA/ACC guideline landscape, not merely prior literature; make explicit what the new result changes for practice or guidelines.
- AHA scientific statements and focused updates follow a committee-driven format; contact the editorial office before preparing these — cold unsolicited statements are not accepted.
- Figures must meet AHA graphical standards (vector formats preferred); central illustration or graphical abstract is standard for high-visibility articles.
- Supplemental material should be kept to genuinely supplementary data; core results belong in the main manuscript.
- Reporting guidelines checklists (CONSORT, STROBE, PRISMA, etc.) must be completed and uploaded as submission documents.

## Official-submission checklist

- Search the live site for "Circulation author instructions" on the AHA Journals site and follow the current version, not a cached or third-party copy.
- Re-check article-type classification (Original Research, Scientific Statement, Research Letter, Clinical Perspective), as length and format limits differ by type.
- Confirm trial or study registration (ClinicalTrials.gov or equivalent), ethics/IRB/consent documentation, and the data-sharing/availability statement.
- Verify the applicable reporting guideline and upload the completed checklist (CONSORT, STROBE, PRISMA, ARRIVE, TRIPOD, or equivalent).
- Confirm competing-interests, funding disclosures, and AHA conflict-of-interest policy compliance for all authors.
- Re-check the current AI-use disclosure requirements and open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result directly informs AHA guidelines, clinical decision-making, or cardiovascular public health at scale.
- [ ] The contribution is stated as a definitive clinical finding, mechanistic advance, or practice change — not as a p-value or "first study to."
- [ ] The framing positions the paper against landmark Circulation-published trials or statements in this disease area.
- [ ] The applicable reporting guideline checklist is complete, and registration/consent documents are ready for upload.
- [ ] Human translational relevance is explicitly demonstrated, not implied, for any mechanistic paper.
- [ ] Central illustration or graphical abstract is prepared per AHA graphical standards.

## Common desk-reject triggers

- Single-center retrospective audits or small pilot studies without a pre-specified hypothesis or sufficient sample size for the primary endpoint.
- Mechanistic animal or cell-based studies with no human-data bridge, biomarker, or genetic corroboration.
- Observational studies with inadequate confounding control or no pre-specified analysis plan presented as hypothesis-testing.
- Scope mismatch: papers on non-cardiovascular clinical endpoints or basic molecular biology with only tangential cardiac framing.
- Missing or incomplete reporting guideline checklist, absent trial registration, or unresolved ethics/consent documentation.

## Re-routing decision

- A cardiovascular RCT or clinical trial primarily relevant to ACC device/intervention guidelines → `journal-of-the-american-college-of-cardiology` (JACC), which has a stronger interventional cardiology and device culture.
- A European-led multinational trial aligned with ESC guidelines → `european-heart-journal` (EHJ), the ESC flagship.
- A cardiovascular mechanism study with strong molecular biology (genetic mouse models, single-cell genomics) but limited clinical translation → `nature-medicine` or `journal-of-clinical-investigation`.
- A general cardiology clinical trial not clearing Circulation's significance bar → JACC Cardiovascular Interventions, JACC Heart Failure, or Circulation subspecialty journals (Heart Rhythm, Circulation: Heart Failure).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Circulation
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the RCT registration / reporting guideline / translational bridge clear Circulation's AHA significance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / structured abstract / CONSORT or equivalent / trial registration / AHA conflict-of-interest / data-sharing>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
