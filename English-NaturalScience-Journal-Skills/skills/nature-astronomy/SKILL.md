---
name: nature-astronomy
description: Use when targeting Nature Astronomy (Nat Astron) or deciding whether an astronomy or astrophysics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Astronomy (nature-astronomy)

## Journal positioning

Nature Astronomy is a Springer Nature journal covering the full breadth of astronomy, astrophysics, and planetary science, publishing results whose conceptual significance extends well beyond a single sub-field. The readership spans the entire astronomical community plus interested physical scientists, so results must be framed for an audience that is expert but may not be specialists in the narrow technique or object class. The journal competes with Nature, Science, and Cell for papers that define or redirect a field; incremental advances or purely archival catalogues do not belong here.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature submission portal.

## When to trigger

- The author names Nature Astronomy or Nat Astron as the target venue.
- A manuscript reports a conceptual first — a new class of object, a new physical mechanism, or a result that forces revision of an established picture — and the author is weighing it against Nature, Science, or the-astrophysical-journal.
- An archival observational or simulation campaign has a single headline result of broad significance that can be told in a short, narrative-driven paper.
- The author needs Nature Astronomy's desk-reject risks and a credible alternative-venue list.

## Scope & topic fit

- Discovery-class results in observational or theoretical astrophysics (multi-messenger events, transient phenomena, first detections).
- Cosmological results that revise parameters, probe new epochs, or stress-test the standard model.
- Planetary science and Solar System results with connections to broader astrophysical understanding.
- Instrumentation or survey milestones only when the science extracted constitutes the primary advance, not the instrument itself.
- High-impact results from large facilities (JWST, EHT, LIGO/Virgo/KAGRA, Gaia, CMB telescopes) that require broad contextualization.

## Method & evidence bar

- Observational claims require rigorous treatment of systematics, calibration, and statistical significance; upper limits and non-detections must be properly framed.
- Simulations must be benchmarked against observations and the physical assumptions clearly defended.
- Multi-messenger or multi-wavelength analyses must demonstrate synergy beyond co-location; each data stream must independently constrain the claim.
- Statistical significance thresholds should follow community conventions for the sub-field; do not over-claim marginal detections.
- Data, code, and model outputs underlying the central claim should be made publicly available; re-check the current data availability policy.

## Structure & house style

- Nature Astronomy publishes Articles and Letters (check current article-type definitions on the live site); framing must match the chosen type.
- The first paragraph must hook the broad community: state the open question, why it matters to astronomy, and what this result delivers — before any technical detail.
- A structured Methods section (often placed after the main text) carries the technical and statistical details, keeping the narrative uncluttered.
- Extended Data figures (numbered separately) bear the validation and supplementary evidence; the main figures tell the story.
- A Nature-family reporting summary and data/code availability statement are required; re-check the current checklist.
- Abstract is unstructured and must be self-contained for a broad science readership; avoid jargon in the first sentence.

## Official-submission checklist

- Search the live site for "Nature Astronomy author instructions" and follow the current Springer Nature version.
- Re-check article type (Article vs. Letter vs. Comment/Brief Communication), length limits for main text and abstract, and figure count.
- Confirm Extended Data figure policy, reporting summary, and data/code availability requirements.
- Verify competing-interests disclosure, author-contribution statement, AI-use policy, and preprint/embargo policy.
- Re-check the current open-access options and licensing requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the conceptual advance and why it matters beyond the immediate sub-field.
- [ ] The contribution is framed as a physical insight or discovery, not as a dataset or a pipeline.
- [ ] The first paragraph of the main text positions the result against the current state of the field without assuming sub-field expertise.
- [ ] Methods, systematics, and statistical treatment are in the Methods section or Extended Data, not cluttering the narrative.
- [ ] Reporting summary, data/code availability, and author contributions are complete and match current policy.

## Common desk-reject triggers

- A narrowly scoped catalogue, survey data release, or pipeline paper without a headline science result of broad significance.
- A result already reported or superseded by concurrent preprints, or where the claimed novelty rests on a literature gap the editor can readily fill.
- Framing pitched at specialists ("we update the photometric redshift calibration of X survey") rather than the broad astronomy community.
- Statistical significance marginal by community standards, or systematics inadequately addressed in the main text.
- Overlong main text that buries the conceptual advance in observational detail — more appropriate for the-astrophysical-journal or monthly-notices-of-the-royal-astronomical-society.

## Re-routing decision

- Archival, technically detailed, or longer observational/simulation papers without a single broad headline → `the-astrophysical-journal` (ApJ for full articles, ApJL for urgent results) or `monthly-notices-of-the-royal-astronomical-society`.
- Result rises to the level of Nature or Science (cross-disciplinary significance, not just astrophysics) → consider those general venues directly.
- Instrumentation or mission-description emphasis → Publications of the Astronomical Society of the Pacific or relevant facility journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Astronomy
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result constitute a conceptual advance with adequate statistical and systematic treatment?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / Extended Data / reporting summary / data-code / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
