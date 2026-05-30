---
name: journal-of-the-american-college-of-cardiology
description: Use when targeting Journal of the American College of Cardiology (JACC) or deciding whether a cardiovascular manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of the American College of Cardiology (journal-of-the-american-college-of-cardiology)

## Journal positioning

The Journal of the American College of Cardiology is the official flagship of the ACC and the leading venue for cardiovascular medicine that bridges interventional cardiology, imaging, heart failure, electrophysiology, and preventive cardiology under one roof. Unlike Circulation's broad AHA mandate, JACC carries a distinctively proceduralist and device-oriented culture alongside large clinical trials — making it the first-choice venue for coronary intervention, structural heart disease, advanced cardiac imaging, and ACC guideline-informing evidence. The readership is the ACC membership: interventional and general cardiologists, cardiac imaging specialists, heart-failure subspecialists, and the trainees who move across all these areas.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACC / JACC publisher site and submission system.

## When to trigger

- The author names JACC as the target venue for a cardiovascular clinical or translational paper.
- A paper on coronary intervention, structural heart disease, cardiac imaging, or device therapy needs venue selection among JACC, Circulation, and EHJ.
- A manuscript covering an ACC guideline priority (stable ischemic heart disease, valvular disease, cardiac risk stratification) needs framing guidance.
- The author needs JACC's desk-reject risks and a ranked alternative — including the JACC subspecialty family — before submitting.

## Scope & topic fit

- Clinical trials and large registry studies in interventional cardiology, coronary and structural heart disease, with direct implications for ACC clinical competency statements or guideline updates.
- Cardiovascular imaging advances (echocardiography, CT, MRI, nuclear) where diagnostic performance or risk-stratification benefit is rigorously quantified.
- Heart failure (device, pharmacological, advanced therapies) trials and registry-based analyses at scale sufficient to inform ACC Heart Failure Guidelines.
- Preventive cardiology, risk-stratification tools, lipid management, and cardiometabolic studies aligned with ACC Prevention Guidelines.
- ACC-authored or ACC-endorsed expert consensus documents and appropriate-use criteria (typically invited; concept approval required before preparation).

## Method & evidence bar

- Randomized trials must be registered, CONSORT-compliant, and powered for a pre-specified primary endpoint with clinical relevance to cardiology practice; superiority vs. non-inferiority framing must be pre-specified.
- Observational studies and registries (including ACC's own NCDR data) require detailed covariate adjustment and explicit identification of the clinical question; post-hoc, unplanned subgroup analyses are held to a strict inferential standard.
- Imaging and diagnostic studies must report sensitivity/specificity, AUC/C-statistic, and calibration where applicable; TRIPOD checklist required for prediction models.
- Device and procedural studies should clearly separate operator-volume/center effects, describe learning-curve considerations, and pre-specify major adverse cardiac event definitions.
- Statistical rigor: current standards for time-to-event analysis, competing risks, and multiple testing apply; raw p-values without confidence intervals or effect sizes are insufficient.
- ARRIVE for animal studies; reporting guideline checklist must accompany submission.

## Structure & house style

- Structured abstract (Background / Objectives / Methods / Results / Conclusions) with quantitative primary results including confidence intervals in Conclusions.
- Introduction must frame the paper relative to relevant ACC/AHA guidelines, stating explicitly which guideline gap or evidence gap the study addresses.
- The "Key Points" or "Perspectives" box (check current format requirements) should summarize: What is Known, What is New, and What are the Implications — this is JACC-specific and must be sharp, not generic.
- Central Illustration with a brief legend is a JACC standard feature for high-profile articles; it should capture the conceptual advance or key result visually.
- Supplementary appendices are permitted but core efficacy and safety data must remain in the main text; do not hide primary outcomes in supplementary tables.
- JACC subspecialty journals (JACC Cardiovascular Interventions, JACC Cardiovascular Imaging, JACC Heart Failure, JACC: Clinical Electrophysiology, JACC: CardioOncology) are not fallback options for the same paper — they are distinct editorial identities with separate scope.

## Official-submission checklist

- Search the live site for "JACC author instructions" on the ACC/JACC publisher platform and follow the current version.
- Re-check article-type classification (Original Investigation, State-of-the-Art Review, Research Correspondence) and confirm length/figure limits for each type.
- Confirm prospective trial or study registration and upload the relevant registration documentation.
- Complete and upload the applicable reporting guideline checklist (CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or equivalent).
- Verify ACC conflict-of-interest disclosure requirements for all authors, including relevant industry relationships.
- Re-check "Key Points" / "Perspectives" box format, Central Illustration specifications, and any graphical abstract requirements.
- Confirm data-sharing and code-availability statement, open-access options, and current AI-use disclosure policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this finding informs ACC guidelines, cardiology clinical practice, or competency standards.
- [ ] The contribution is framed as definitive evidence, a validated tool, or a mechanism advance — not as a registry description or exploratory pilot.
- [ ] The "Key Points" box concisely distinguishes this paper's contribution from the most recent JACC or Circulation trial in the same area.
- [ ] A Central Illustration is drafted and captures the main conceptual or result message in one figure.
- [ ] Registration, reporting guideline checklist, ethics/consent, and ACC COI disclosure are complete.
- [ ] Subspecialty scope mismatch is checked: if the primary topic is arrhythmia, imaging, or heart-failure device, the JACC subspecialty journal may be the better fit.

## Common desk-reject triggers

- Small single-center procedural series or registries without pre-specified hypotheses, adequate controls, or sufficient sample size to draw practice-relevant conclusions.
- Papers framed as cardiology but with primary endpoints in non-cardiovascular domains (e.g., renal, pulmonary) that belong to subspecialty journals.
- Missing or generic "Key Points" / "Perspectives" box — JACC editors check this explicitly.
- An observational study with severe confounding and no sensitivity analyses, presented as providing clinical guidance.
- Prior publication of core results as a conference abstract in a form that makes the manuscript derivative rather than novel.

## Re-routing decision

- A large multi-society cardiovascular RCT with AHA co-leadership or an AHA scientific statement → `circulation` (AHA flagship; stronger AHA-aligned readership).
- A European multinational trial explicitly aligned with ESC guidelines → `european-heart-journal` (ESC flagship audience).
- A device or procedure trial with primary interventional scope but exceeding JACC's bar → consider JACC Cardiovascular Interventions (separate editorial board).
- A translational mechanism paper with clinical data bridge but insufficient trial scope → `journal-of-clinical-investigation` or `nature-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of the American College of Cardiology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the trial registration / Key Points / Central Illustration / reporting guideline clear the JACC ACC-focused bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / structured abstract / Key Points box / Central Illustration / CONSORT or equivalent / ACC COI / data-sharing>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
