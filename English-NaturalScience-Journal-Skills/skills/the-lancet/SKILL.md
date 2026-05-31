---
name: the-lancet
description: Use when targeting The Lancet or deciding whether a clinical medicine or global-health manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Lancet (the-lancet)

## Journal positioning

The Lancet is one of the world's oldest and most influential general medical journals, published by Elsevier. It publishes practice-changing and policy-changing clinical and global-health evidence, with an explicit commitment to health equity, global burden of disease, and the social determinants of health. The readership spans clinicians, public-health practitioners, policymakers, and health systems researchers worldwide. Papers that merely confirm existing practice without shifting guidelines or informing policy do not belong here.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names The Lancet as the target venue for a clinical trial, systematic review, or global-health analysis.
- A manuscript has potential practice- or policy-changing implications but needs framing around equity, global-health burden, or health-systems impact.
- A clinical-medicine paper needs to distinguish The Lancet's editorial culture from NEJM or JAMA before deciding where to submit.
- The author needs The Lancet's desk-reject risks and credible alternatives before submitting.

## Scope & topic fit

- Large, well-powered randomised controlled trials with definitive superiority or non-inferiority results affecting clinical practice at scale.
- Systematic reviews and meta-analyses (PRISMA-compliant) that resolve a contested clinical question or establish a new evidence base.
- Global-health burden analyses, disease modelling, and epidemiological surveillance with policy implications for low- and middle-income countries.
- Health equity research: interventions or analyses addressing disparities across geography, income, race, sex, or other social determinants.
- Public-health emergencies, outbreak investigations, and pandemic-response science that reaches a global clinical and policy audience.
- Landmark observational cohort studies with prospective design and precise, adequately adjusted effect estimates.

## Method & evidence bar

- Randomised trials must be pre-registered (ClinicalTrials.gov or WHO ICTRP equivalent), follow CONSORT reporting in full, and have an independent data-safety monitoring board for longer-horizon studies.
- Systematic reviews and meta-analyses require PRISMA adherence; protocol registration in PROSPERO or equivalent is expected; GRADE assessment of evidence quality is strongly encouraged.
- Observational studies require STROBE reporting and explicit discussion of residual confounding; propensity-score or multivariable adjustment alone does not satisfy the standard.
- The significance bar is definitiveness or paradigm-shift at population scale, not statistical significance in a convenience sample.
- Ethics approval and participant informed-consent documentation are mandatory; ICMJE authorship criteria must be satisfied and author contributions declared.
- Data sharing: a data-sharing statement is required; sharing individual participant data (IPD) for trials is strongly encouraged and increasingly expected.

## Structure & house style

- The Lancet uses article types including Articles, Letters, Correspondence, Comment, and Review; choose the type that matches scope and length—re-check current word limits.
- The abstract for an Article is structured (background, methods, findings, interpretation) and must close with a funding statement.
- The opening paragraph of an Article must situate the work in current practice and articulate the evidence gap the study fills.
- An "Added value of this study" summary panel (what is already known, what this study adds) is required for Articles and Reviews.
- Statistical reporting must include absolute as well as relative effect measures; confidence intervals are mandatory; p-values alone are insufficient.
- Figures should be colour-blind-friendly and publication-ready; maps showing global data are highly valued editorially.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The Lancet information for authors" and follow the current Elsevier/Lancet version.
- Re-check article type definitions and current word/figure limits; re-check abstract structure requirements and the "Added value" panel format.
- Confirm trial or review registration number, ethics approval reference, and informed-consent statement are included.
- Confirm the data-sharing statement specifies what data will be shared, when, how, and with whom.
- Re-check competing-interests declaration (all authors), funding disclosure, ICMJE author-contribution statement, and AI-use disclosure policy.
- Confirm CONSORT (trials) or PRISMA (reviews) or STROBE (observational) checklist is submitted as a supplementary file.
- Re-check open-access/APC options, licensing terms, and preprint policy (The Lancet permits preprints; confirm current guidance).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this finding changes clinical practice, public-health policy, or health-equity understanding at a population level.
- [ ] The contribution is framed as definitive evidence, practice shift, or policy insight—not as a "first-ever" claim or a p-value.
- [ ] The introduction positions the paper against the most relevant prior evidence, with an explicit statement of the remaining evidence gap.
- [ ] Reporting guideline checklist (CONSORT/PRISMA/STROBE) is complete and attached; registration number is cited in the methods.
- [ ] The "Added value" panel is drafted and accurately distinguishes this study's contribution from the existing literature.
- [ ] Global-health or equity framing is authentic and data-supported, not appended as a rhetorical gesture.

## Common desk-reject triggers

- Trials that are not pre-registered, lack a CONSORT flow diagram, or have a sample size powered only for a surrogate endpoint with no clinical-outcome data.
- Systematic reviews without PROSPERO registration or PRISMA adherence, or meta-analyses dominated by high-risk-of-bias studies without sensitivity analysis.
- Single-centre or small-sample studies that do not establish a definitively new finding at scale.
- Observational studies framed as causal without credible identification strategy, or with STROBE-non-compliant reporting.
- Absence of a data-sharing statement or an ethics-approval reference; missing ICMJE authorship contributions.
- Global-health framing that is superficial—"this matters globally" asserted without burden-of-disease data or LMICcontext.

## Re-routing decision

- Clinically definitive but more specialised in disease area → `the-lancet-oncology`, `the-lancet-infectious-diseases`, or `the-lancet-neurology` for condition-specific practice change.
- US-centric clinical trial with a rigorous AMA-style structured abstract → `jama` or `nejm`.
- Methodologically rigorous but emphasis on open data, EBM critique, or patient/public involvement → `the-bmj`.
- Translational mechanism-to-trial story with biological depth → `nature-medicine`.
- Open-access public-health focus with lower significance bar → `plos-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet
[Topic tags] <2–3 closest topics>
[Method/evidence] <does trial registration / CONSORT / scale clear The Lancet's practice-change bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / structured abstract / Added-value panel / reporting checklist / data sharing / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
