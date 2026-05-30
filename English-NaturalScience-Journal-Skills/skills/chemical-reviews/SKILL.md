---
name: chemical-reviews
description: Use when targeting Chemical Reviews (Chem Rev) or deciding whether a chemistry review manuscript fits this ACS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics. NOTE: Chemical Reviews is a largely INVITED venue; unsolicited primary-data manuscripts will be desk-rejected.
---

# Chemical Reviews (chemical-reviews)

## Journal positioning

Chemical Reviews, published by the American Chemical Society, is one of the most authoritative and widely cited venues for comprehensive review articles across all areas of chemistry. The journal publishes definitive, exhaustive treatments of mature or rapidly evolving research areas — not opinion pieces, not progress reports, and not primary research articles. Chemical Reviews is a **largely invited venue**: the majority of reviews are commissioned by the editors from leaders in a sub-field; unsolicited review proposals are accepted but must clear a higher bar of timeliness, comprehensiveness, and author authority. Submitting primary experimental data here is a categorical mismatch.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACS submission system.

## When to trigger

- The author has received an invitation from Chemical Reviews editors, or is preparing an unsolicited review proposal.
- A comprehensive review of a chemistry sub-field needs evaluation against the Chem Rev standard (vs. `chemical-society-reviews` or `accounts-of-chemical-research`).
- A colleague asks whether a long, comprehensive manuscript is appropriate for Chemical Reviews.
- The author needs to understand why primary data or short reviews should be redirected.

## Scope & topic fit

- Comprehensive, critical surveys of an entire research area: synthesis, structure, mechanism, properties, and applications integrated across the literature.
- Thematic reviews that cover a major class of reactions, reagents, materials, or biological systems from a chemistry-centred perspective.
- Authoritative treatments of interdisciplinary areas where chemistry is central: chemical biology, materials chemistry, energy storage and conversion, environmental chemistry.
- Timely reviews of rapidly developing fields where a definitive synthesis of scattered primary literature adds high community value.
- Do NOT submit: progress reports on a single group's work (those belong in `accounts-of-chemical-research`), short thematic reviews (those may fit `chemical-society-reviews`), or primary research papers of any kind.

## Method & evidence bar

- Comprehensiveness: the review must cover the primary literature with critical, not merely descriptive, analysis; gaps, controversies, and unresolved questions should be explicitly identified.
- Critical assessment: conflicting experimental results must be reconciled or the disagreement explained; the review should guide a non-specialist to an accurate picture of the field.
- Currency: the literature coverage must extend to recent publications; editors will check that newly published key papers are included.
- Citation accuracy: all cited papers must be correctly described; mischaracterisation of prior work is a serious quality failure.
- Length: Chemical Reviews reviews are long; re-check the current length expectation with the editors, as it varies by topic and invitation scope.

## Structure & house style

- A substantial Introduction motivates the review: why this topic now, what questions it addresses, what the scope includes and explicitly excludes.
- Body sections are organised thematically, not chronologically; each section should carry a sub-thesis, not just a literature dump.
- A Conclusions and Outlook section identifies open questions, future directions, and the authors' informed opinion on where the field is heading.
- Figures, schemes, and tables should be original where possible; reproduced material requires rights clearance.
- ACS author guidelines govern citation style and formatting; re-check current requirements for SI, data availability, and figure permissions.

## Official-submission checklist

- Search the live site for "Chemical Reviews author guidelines" and follow the current ACS version.
- For unsolicited reviews: submit a proposal (scope outline, author qualifications, estimated length and timeline) before a full manuscript, per ACS editorial practice.
- Re-check current length norms, figure/scheme count, and SI policy with the editorial office.
- Confirm rights clearance process for figures reproduced from primary literature.
- Verify conflict-of-interest, funding disclosure, and AI-use policy requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] This manuscript is a comprehensive critical review, not a primary research paper or a progress report on one group's work.
- [ ] If unsolicited: a proposal was submitted and received positive editorial response before the full manuscript was written.
- [ ] The literature coverage is comprehensive (not cherry-picked), critical (not merely descriptive), and current.
- [ ] Conflicts, controversies, and open questions are explicitly addressed, not glossed over.
- [ ] Figures reproduced from the primary literature have rights clearance (or are original).

## Common desk-reject triggers

- Submission of a primary research paper (any article reporting new experimental or computational results not yet published).
- An unsolicited full manuscript without prior editorial engagement or a favourable proposal response.
- A review that covers only one group's contributions rather than the full field — this belongs in `accounts-of-chemical-research`.
- A short thematic overview (minireviews, highlights) — these belong in `chemical-society-reviews`, ACS Central Science, or similar venues.
- A review with literature coverage that stops substantially short of recent developments, missing key papers that editors can identify quickly.

## Re-routing decision

- Primary research data, new reactions, or new compounds → `journal-of-the-american-chemical-society`, `angewandte-chemie-international-edition`, or `nature-chemistry` depending on significance.
- A concise account of the author's own research program → `accounts-of-chemical-research`.
- A shorter critical or tutorial review → `chemical-society-reviews` (RSC) or ACS Chemical Reviews' sibling journals (e.g., Chemical Reviews Letters if it exists — re-check the current ACS portfolio).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Chemical Reviews
[Topic tags] <2–3 closest topics>
[Method/evidence] <is this a comprehensive critical review with current literature coverage — and is it invited or proposal-approved?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <proposal submission process / length / figure rights / disclosure / AI-use policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
