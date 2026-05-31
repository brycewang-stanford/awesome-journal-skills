---
name: european-heart-journal
description: Use when targeting European Heart Journal (EHJ) or deciding whether a cardiovascular manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# European Heart Journal (european-heart-journal)

## Journal positioning

The European Heart Journal is the flagship journal of the European Society of Cardiology, published by Oxford University Press, and the premier cardiovascular venue for European and international readership. EHJ's editorial identity is built around ESC guideline-informing clinical trials, pan-European registry analyses, and large-scale epidemiology — with an explicit ESC-member and multinational-trial culture that distinguishes it from Circulation (AHA) and JACC (ACC). Translational papers are welcome but must carry clear clinical relevance; registry data leveraging EuroSCORE, EuroHeart, or ESC-sponsored databases have a natural home here. The readership is the broad ESC membership: European and international cardiologists, internists, and cardiovascular researchers who follow ESC guideline cycles.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ESC / Oxford University Press EHJ platform.

## When to trigger

- The author names EHJ or the ESC as the target venue for a cardiovascular manuscript.
- A multinational European cardiovascular trial or cohort study needs venue selection among EHJ, Circulation, and JACC.
- A paper linked to ESC guideline development, position papers, or ESC consensus documents is being prepared.
- The author needs EHJ's desk-reject risks and alternative-venue guidance before submitting.

## Scope & topic fit

- Randomized controlled trials in cardiovascular medicine with multinational enrollment and direct relevance to ESC guideline recommendations across cardiology subspecialties.
- Large pan-European or international registry analyses (ESC EORP, EuroHeart surveys, national registries) that quantify guideline adherence, outcomes, and treatment gaps at population scale.
- ESC clinical practice guidelines, focused updates, position papers, and expert consensus documents (these require prior ESC Task Force or editorial engagement; unsolicited committee documents are not accepted).
- Cardiovascular epidemiology and prevention with a European or global public-health dimension; risk-score development or validation in European cohorts.
- Translational and mechanistic cardiovascular science where human data (biomarkers, genetics, imaging) provides the primary evidence layer, with animal/in vitro data as mechanistic support.
- Cardiovascular imaging (CT angiography, echocardiography, CMR) with demonstrated impact on diagnosis, risk stratification, or management aligned with ESC imaging recommendations.

## Method & evidence bar

- RCTs must be prospectively registered, CONSORT-compliant, and pre-specify the primary endpoint and analysis plan; multinational enrollment and ESC-relevant comparators are strongly valued.
- Registry and observational studies require pre-specified exposure and outcome definitions, propensity-score or multivariable confounding control, and clinical rather than merely statistical significance; ESC-sponsored or -endorsed registries are a natural fit.
- Prediction models and risk scores must follow TRIPOD reporting standards with external validation in an independent cohort; incremental discrimination beyond existing ESC risk tools must be demonstrated.
- Mechanistic papers must include human biomarker, genetic, or imaging evidence as the primary evidentiary layer; rodent-only or cell-only papers without human corroboration will not clear EHJ's bar.
- Reporting guideline checklists (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE) must be completed and uploaded; EHJ editors check compliance explicitly.
- Statistical standards follow current ESC/EHR committee standards; Bayesian and adaptive trial designs are acceptable with appropriate pre-specification.

## Structure & house style

- Structured abstract (Background / Methods / Results / Conclusions) with absolute and relative effect sizes and confidence intervals reported in the Conclusions section.
- The introduction must reference the relevant ESC guideline or position paper landscape, stating which guideline gap or evidence uncertainty the study addresses; pure literature-gap framing without guideline context is insufficient.
- "What's New" or "Key Message" panel (check current format) is an EHJ expectation — it must capture what this paper adds to ESC guideline evidence, not a generic novelty claim.
- Graphical abstract is standard and expected for all original research; it should summarize the study design, key result, and clinical implication in a single figure.
- Supplementary data files should carry sensitivity analyses and secondary outcomes; primary efficacy and safety results must be in the main text.
- Oxford University Press formatting (OUP reference style, figure resolution, and file format specifications) — re-check current OUP/EHJ guidelines at submission.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "European Heart Journal author instructions" on the OUP/ESC platform and follow the current version.
- Re-check article-type classification (Original Article, Clinical Research, ESC Guidelines document, Research Correspondence, Editorial) and confirm current length and figure limits.
- Confirm prospective trial or study pre-registration; upload ethics/IRB and patient-consent documentation.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or equivalent).
- Verify ESC conflict-of-interest disclosure requirements, which align with ESC guidelines committee standards.
- Re-check OUP formatting requirements, graphical abstract specifications, and any "Key Message" panel format.
- Confirm data-sharing/availability statement, open-access and licensing options (OUP hybrid and OA policies), and current AI-use disclosure policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result informs ESC guideline development or European cardiovascular clinical practice.
- [ ] The contribution is framed as definitive evidence, a validated prediction tool, or a mechanism advance with human translation — not an exploratory registry description.
- [ ] The "Key Message" panel concisely distinguishes this paper's contribution from the most recent EHJ or ESC guideline evidence on this topic.
- [ ] A graphical abstract is prepared summarizing study design, main result, and clinical implication.
- [ ] Registration, reporting guideline checklist, ethics/consent, and ESC COI disclosures are complete for all authors.
- [ ] Multinational or European scope is explicit in the methods and discussion; single-country studies of limited scope are flagged for rerouting consideration.

## Common desk-reject triggers

- Single-country, single-center studies too modest in scope to inform ESC guideline evidence or European-scale practice; insufficient sample size for the stated primary endpoint.
- Observational analyses from non-ESC or non-European registries without explicit justification of relevance to ESC clinical practice.
- Missing "Key Message" panel or a generic graphical abstract that does not capture the clinical implication — EHJ editors check both.
- Mechanistic papers without human evidence (biomarker, genetic, or imaging data) as the primary evidentiary layer.
- Incomplete or absent reporting guideline checklist; missing trial registration; unresolved COI documentation for any author.

## Re-routing decision

- A cardiovascular trial with primary AHA co-leadership or strong North American enrollment majority → `circulation` (AHA flagship; AHA readership better aligned).
- An ACC guideline-informing RCT or device/intervention trial with primary ACC context → `journal-of-the-american-college-of-cardiology` (JACC, ACC flagship).
- A cardiovascular mechanism paper without a European/ESC clinical frame → `journal-of-clinical-investigation` or `nature-medicine` for translational depth.
- A smaller European specialty cardiology study (e.g., electrophysiology, congenital) → European Journal of Heart Failure, Europace, or relevant ESC subsidiary journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] European Heart Journal
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the multinational scope / ESC guideline framing / reporting guideline / human-data primary layer clear EHJ's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / structured abstract / Key Message panel / graphical abstract / CONSORT or equivalent / ESC COI / OUP format / data-sharing>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
