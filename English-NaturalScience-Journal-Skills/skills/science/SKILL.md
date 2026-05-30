---
name: science
description: Use when targeting Science (AAAS) or deciding whether a multidisciplinary manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science (science)

## Journal positioning

Science is the flagship weekly journal of the American Association for the Advancement of Science (AAAS), and alongside Nature the most broadly read scientific publication in the world. It publishes Research Articles and shorter Reports (re-check current article-type names) judged on whether they represent a major conceptual advance of significance to scientists across multiple disciplines. Science's US institutional identity and AAAS mission give it a particular interest in science with policy relevance, cross-disciplinary methodology, and societal implications — making it slightly more receptive than Nature to social-scientific or interdisciplinary framing when the empirical standard is met. Editorial triage is aggressive: most manuscripts are rejected without external review.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAAS/Science site and the submission portal.

## When to trigger

- The author names Science as the target venue.
- A manuscript has clear cross-disciplinary significance and the author is choosing between Science, Nature, and PNAS.
- A paper has a policy-relevant or societally significant finding and needs framing that fits Science's AAAS mission.
- The author needs Science's desk-reject patterns and credible alternative routing before submitting.

## Scope & topic fit

- Any natural or formal science field where the result is of broad significance: physics, chemistry, biology, medicine, earth and environmental science, computational science.
- Cross-disciplinary breakthroughs where the combined methodology or finding benefits audiences in at least two distinct scientific communities.
- Findings with direct policy or societal implication — Science is more willing than Nature to frame a result in terms of real-world consequences if the science is unambiguous.
- Technical or methodological breakthroughs that open new experimental or analytical territory for a wide range of disciplines.
- Earth-system science, climate, biodiversity, and conservation results of global consequence.

## Method & evidence bar

- The central claim must be airtight: adequate sample sizes, appropriate statistics with effect sizes reported, independent replication or validation, and full disclosure of alternative explanations considered.
- Reports carry a short, self-contained methods section (or Methods online); Research Articles allow more methodological depth — both must be fully reproducible from the published record.
- Materials and Data Availability statements are required; deposition in community repositories is expected for genomics, structural biology, climate, and related data-intensive fields.
- For clinical or human-participant research: registration, ethics approval, consent, and reporting-guideline compliance (CONSORT, STROBE, PRISMA as applicable) are required.
- Science imposes a Supplementary Materials section for secondary data, validation, and protocols; the main text must stand on its own.

## Structure & house style

- Reports (the short-form article type — re-check current terminology) are tightly length-limited: the advance must be stated and validated in a compact narrative. Re-check current word and figure limits.
- The opening paragraph must frame the scientific problem broadly and state the advance in one sentence accessible to a physicist reading a biology paper and vice versa.
- Science uses unstructured abstracts; the abstract itself is a critical triage document — editors and readers outside the field rely on it heavily.
- A "one-paragraph summary" or structured significance statement may be required at submission (re-check current requirements); this is a primary editorial filter.
- Main figures (re-check current count limits) must tell the story; Supplementary Materials accommodate validation and protocols but should not carry results essential to the main claim.
- References in the main text are limited (re-check count); citation choices signal field positioning.

## Official-submission checklist

- Search the live site for "Science author instructions" or "Science information for authors" and follow the current AAAS version.
- Re-check current article types (Research Article, Report, etc.), word limits, abstract format, and Supplementary Materials policy.
- Re-check data/code/materials availability requirements, community repository expectations, and any field-specific reporting guidelines.
- Re-check ethics/consent/registration requirements, competing-interests disclosure, funding statement, and AI-use disclosure.
- Re-check the preprint policy and whether the manuscript is under embargo at another venue.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence that a chemist, a biologist, and a geoscientist would all find significant — Science editors span all fields and must all agree.
- [ ] The significance statement (or cover letter) makes the cross-disciplinary impact explicit without overselling.
- [ ] The contribution is stated as a conceptual advance, new phenomenon, or decisive evidence — not as "first to show" or a method improvement alone.
- [ ] The opening paragraph requires no specialist vocabulary to convey the core finding.
- [ ] Data, code, and materials availability are confirmed; ethics/registration documentation is ready.
- [ ] The abstract alone is compelling enough to survive a non-specialist triage read.

## Common desk-reject triggers

- The advance is major in its sub-field but does not carry obvious significance outside that community.
- The manuscript is framed as a methods advance without a scientific discovery; methods advances belong in `nature-methods` or `nature-biotechnology` unless the method itself is the major discovery.
- Supplementary Materials carry results essential to evaluating the main claim, making the main text incomplete.
- The opening paragraph assumes deep specialist knowledge; editors in adjacent fields cannot follow the abstract.
- Inadequate reporting: missing statistics, sample sizes, effect sizes, or replication information.

## Re-routing decision

- Broad-significance result, UK/European primary context or Nature brand preference → `nature`.
- Solid, complete multidisciplinary advance below the Science/Nature significance threshold → `pnas`, `science-advances`, or `nature-communications`.
- Open-access required with AAAS-family brand → `science-advances`.
- Cell/molecular biology mechanistic advance with deep validation → `cell`.
- National-significance result from Chinese institutions with global relevance → `national-science-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result clear the cross-disciplinary significance and reproducibility bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / word/figure limit / significance statement / data-code / ethics / reporting guidelines>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
