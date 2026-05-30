---
name: nejm
description: Use when targeting The New England Journal of Medicine (NEJM) or deciding whether a clinical medicine manuscript fits this venue. Encodes the journal's fit, framing, practice-changing evidence bar, CONSORT/registration requirements, house style, official-submission re-check, and desk-reject heuristics.
---

# The New England Journal of Medicine (nejm)

## Journal positioning

The New England Journal of Medicine, published by the Massachusetts Medical Society, is the most widely read and cited general medical journal in the world. It publishes clinical trials, epidemiological studies, and clinical reviews that change or define standard-of-care practice across all of medicine. The NEJM editorial culture is centered on clinical practice impact: a study must be definitive, practice-changing, and broadly relevant to physicians across specialties — not merely statistically significant or methodologically rigorous in the abstract. The readership is the global physician and clinical-researcher community; non-clinicians are a secondary audience. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on nejm.org.

## When to trigger

- The author names NEJM or The New England Journal of Medicine as the target venue.
- A randomized controlled trial, definitive epidemiological study, or landmark diagnostic-accuracy study has clear practice-changing implications across medicine.
- A clinical research team needs to calibrate whether their study meets the NEJM significance bar or should route to The Lancet, JAMA, or a specialty journal.
- The author needs NEJM's specific format requirements (structured abstract, CONSORT, registration) and desk-reject risks before submitting.

## Scope & topic fit

- Randomized controlled trials with definitive efficacy and safety data for interventions relevant across a broad clinical population — these are NEJM's core product.
- Landmark epidemiological studies (large prospective cohorts, definitive case-control studies) that establish causal links between exposures and clinical outcomes at population scale.
- Diagnostic-accuracy studies for novel biomarkers or imaging strategies when the population and clinical implications are broad and the design is definitive.
- Device and procedure trials: non-inferiority, superiority, or equivalence trials for surgical interventions, devices, or procedures when the clinical impact is field-defining.
- Global health and pandemic-response studies with broad public-health implications, including vaccine trials, outbreak surveillance, and therapeutic trials in high-burden diseases.
- Case Reports and Case Records are a distinct NEJM tradition (Case Records of the Massachusetts General Hospital) — check current editorial policy for unsolicited case submissions.

## Method & evidence bar

- Practice-changing evidence is the editorial standard: a positive RCT must be definitive (adequately powered, pre-specified primary endpoint, appropriate control arm), not exploratory or hypothesis-generating.
- Trial registration is mandatory: all clinical trials must be prospectively registered in a WHO-approved primary registry (ClinicalTrials.gov or equivalent) prior to enrollment; NEJM enforces this at submission.
- CONSORT reporting is required for randomized trials; STROBE for observational studies; STARD for diagnostic studies; PRISMA for systematic reviews and meta-analyses — the appropriate checklist must accompany submission.
- Pre-specified analysis plans: primary endpoints, secondary endpoints, subgroup analyses, and statistical methods must be pre-specified; post-hoc subgroup fishing is a desk-reject trigger.
- Safety data: all efficacy trials must provide complete adverse-event reporting; NEJM applies a high standard for safety characterization.

## Structure & house style

- NEJM uses a **structured abstract** for Original Articles: Background, Methods, Results, Conclusions — each section is mandatory and has implied length norms. Unstructured abstracts are not used for clinical trials.
- The structured abstract must convey the trial design, population, intervention, primary endpoint, key result with effect size and confidence interval, and clinical conclusion — not p-values alone.
- The introduction should be brief (2–3 paragraphs) and frame the clinical gap directly; NEJM reads write for a generalist physician, not a subspecialist.
- Tables and figures must be self-contained; CONSORT flow diagram is required for trials.
- Supplementary appendix carries extended methods, additional analyses, and supplementary tables; the main paper must be readable without it.
- Conflict of interest and funding disclosures are prominently formatted and published alongside the article.

## Official-submission checklist

- Search the live site for "NEJM information for authors" and follow the current Massachusetts Medical Society version.
- Confirm trial registration: registry name, trial number, and date of registration (must be prior to first patient enrollment) must be stated in the Methods.
- Attach the completed CONSORT checklist (for RCTs), STROBE (observational), STARD (diagnostic), or PRISMA (systematic review/meta-analysis) as appropriate.
- Re-check article-type requirements: Original Article, Brief Report, Clinical Practice, Review Article, Case Record, Perspective, Sounding Board — each has distinct format and length norms.
- Verify competing-interests disclosures: NEJM requires comprehensive conflict-of-interest forms for all authors and sometimes for editorialists; the ICMJE form is typically used.
- Confirm data-sharing: NEJM adheres to the ICMJE data-sharing policy — trials must include a data-sharing statement specifying what data will be shared, with whom, and when.
- Check AI-use disclosure, IRB/ethics approval, informed consent documentation, and any DSMB (Data Safety Monitoring Board) statement for trials.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what clinical practice this paper changes and for which patient population — if this cannot be stated clearly, the paper may not be NEJM-tier.
- [ ] The trial is prospectively registered with a WHO-approved registry; the registration number and date appear in the manuscript.
- [ ] The CONSORT (or equivalent) checklist is completed, and the CONSORT flow diagram is ready as a figure.
- [ ] The primary endpoint is pre-specified and clearly distinguished from secondary and exploratory endpoints in the analysis plan.
- [ ] The structured abstract is drafted with all four sections (Background, Methods, Results, Conclusions) in NEJM format; effect size with 95% CI is stated in Results.
- [ ] Competing-interests and data-sharing statements are prepared for all authors.

## Common desk-reject triggers

- Trials that are not prospectively registered, or registered after enrollment began — NEJM enforces this without exception.
- Studies that are adequately powered but do not produce practice-changing findings: a well-conducted trial of a marginal intervention is not NEJM-tier.
- Post-hoc subgroup analyses presented as primary findings without pre-specification — immediately flagged as potentially inappropriate inference.
- Missing CONSORT checklist or a CONSORT flow diagram that does not account for all randomized participants.
- Observational studies framed with causal language without a credible epidemiological design (propensity matching alone is insufficient for NEJM-level causal inference claims).
- Single-center trials for conditions where multicenter evidence is expected — underpowered or ungeneralizable designs for the significance level claimed.

## Re-routing decision

- Landmark clinical evidence in oncology → `the-lancet-oncology` or `journal-of-clinical-oncology`.
- High-impact cardiology trial → `circulation` or `european-heart-journal`.
- Global-health or policy-focused clinical study → `the-lancet` or `jama`.
- Translational (mechanism-to-clinic) framing → `nature-medicine` or `science-translational-medicine`.
- Solid but not paradigm-shifting → `jama`, `the-bmj`, or `annals-of-internal-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The New England Journal of Medicine
[Topic tags] <2–3 closest topics>
[Method/evidence] <is this practice-changing, adequately powered, pre-registered, and CONSORT-compliant?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <trial registration / CONSORT checklist / structured abstract / data sharing / COI / IRB / article type>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
