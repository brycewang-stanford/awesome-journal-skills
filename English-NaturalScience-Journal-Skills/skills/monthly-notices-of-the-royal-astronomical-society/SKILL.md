---
name: monthly-notices-of-the-royal-astronomical-society
description: Use when targeting Monthly Notices of the Royal Astronomical Society (MNRAS) or deciding whether an astronomy manuscript fits this RAS/OUP venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Monthly Notices of the Royal Astronomical Society (monthly-notices-of-the-royal-astronomical-society)

## Journal positioning

Monthly Notices of the Royal Astronomical Society is published by Oxford University Press on behalf of the Royal Astronomical Society and is one of the world's principal archival journals for astronomy and astrophysics, covering observational, theoretical, and computational work across all sub-fields. MNRAS is a broad-scope workhorse comparable in positioning to ApJ: it rewards completeness, methodological rigour, and thorough characterisation of uncertainties over narrative novelty. The journal has a strong European, Southern-hemisphere, and radio/optical-survey community base, though its scope is fully international. Papers do not need to be conceptual firsts to be published, but they must constitute a meaningful, self-contained contribution.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the OUP/RAS submission portal.

## When to trigger

- The author names MNRAS or Monthly Notices as the target venue.
- An astronomy or astrophysics manuscript is archival quality but not a Nature-tier conceptual headline; the author is choosing between MNRAS and the-astrophysical-journal.
- An observational survey, simulation paper, or statistical analysis needs a broad-scope archival home that will not penalise technical depth.
- The author needs MNRAS's desk-reject risks and alternative-venue guidance.

## Scope & topic fit

- Observational astronomy across all wavelengths: stellar physics, variable stars, stellar populations, extragalactic astronomy, galaxy surveys, large-scale structure, cosmology.
- Theoretical and numerical astrophysics: N-body/hydrodynamic simulations, semi-analytic models, analytic theory across all sub-fields.
- Radio, optical, infrared, X-ray, and high-energy astrophysics; Solar System science.
- Astrometry and survey characterisation when the scientific analysis is present and complete.
- Statistical and computational methods for astronomical data, including machine-learning applications with astrophysical validation.

## Method & evidence bar

- The analysis must be self-contained and reproducible: data reduction and calibration steps, software used, and parameter choices must be described in sufficient detail.
- Systematic and statistical uncertainties must both be reported and propagated; selection effects in survey data must be characterised.
- Simulations require statement of physical setup, numerical resolution, and convergence or resolution tests.
- MNRAS uses referee review; revisions are expected to address all referee comments; the review process is not as editorially curated as Nature-family journals.
- Data and code availability is encouraged and increasingly expected; re-check the current OUP/RAS policy.

## Structure & house style

- Article length is relatively unconstrained for full papers; Supporting Information can carry large tables and supplementary figures.
- Abstract is unstructured, typically one paragraph; it must state the method, key result, and quantitative conclusion.
- Section structure follows the standard astronomical format: Introduction, Observations/Data, Analysis/Methods, Results, Discussion, Conclusions.
- LaTeX is the mandatory manuscript format; MNRAS provides its own LaTeX class file (mnras.cls), which must be used.
- References follow the author-year (Harvard) style as implemented in the MNRAS class.
- MNRAS also publishes shorter Letters (MNRAS Letters) for urgent, high-impact results; these have a strict length limit — re-check the current limit.

## Official-submission checklist

- Search the live site for "MNRAS author instructions" or "Monthly Notices information for authors" and follow the current OUP/RAS version.
- Confirm article type: standard paper or MNRAS Letters; re-check the current length limit for Letters.
- Download and use the current mnras.cls LaTeX class file; submissions not using it may be returned.
- Verify data/code availability, Supporting Information policy, and figure resolution and format requirements.
- Check author-contribution, competing-interests, funding, and any ethics/consent requirements.
- Re-check the preprint (arXiv) policy; MNRAS generally permits arXiv posting.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this constitutes a complete, meaningful archival contribution to the field.
- [ ] Systematic and statistical uncertainties are both reported and propagated through to the headline result.
- [ ] Manuscript is formatted with the current mnras.cls LaTeX class file.
- [ ] Abstract states the method and quantitative result concisely.
- [ ] For Letters: manuscript fits within the current length limit and the cover letter justifies urgent publication.

## Common desk-reject triggers

- A Letters submission exceeding the strict length limit without editor pre-approval.
- A paper whose analysis is essentially descriptive (presenting data without interpretation or comparison to models).
- Missing systematic-uncertainty treatment — in survey or photometric work, uncorrected selection effects or calibration issues that make the results unreliable.
- Not using the required MNRAS LaTeX class, causing the manuscript to be returned before review.
- A purely conceptual or speculative paper with no new data, simulation, or methodological content (more appropriate for a review or opinion venue).

## Re-routing decision

- Conceptual advance demanding broad significance narrative for an astronomy audience → `nature-astronomy`.
- AAS-community-focused astrophysics result, or when rapid open-access publication via AAS journals is preferred → `the-astrophysical-journal`.
- Large data product or survey description with minimal per-object analysis → ApJS or a dedicated survey-data venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Monthly Notices of the Royal Astronomical Society
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the analysis meet the archival rigor and completeness bar for MNRAS?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / MNRAS LaTeX class / length / Supporting Information / data-code / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
