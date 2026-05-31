---
name: pnas
description: Use when targeting Proceedings of the National Academy of Sciences (PNAS) or deciding whether a multidisciplinary manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Proceedings of the National Academy of Sciences (pnas)

## Journal positioning

PNAS is the official journal of the National Academy of Sciences (NAS) of the USA and one of the most widely read multidisciplinary scientific journals. It publishes across the full breadth of natural and formal sciences, demanding rigorous evidence and broad significance — but the bar for "broad" is generally set at the discipline or cross-discipline level, not at the everything-must-matter-to-a-geologist level that Nature and Science require. A critical structural feature: the Direct Submission track allows any author to submit without a NAS member endorsement, making PNAS broadly accessible. PNAS is a natural home for important, complete science that has a clear disciplinary audience plus genuine reach into adjacent fields.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the PNAS site (pnas.org) and its submission system.

## When to trigger

- The author names PNAS as the target venue or asks about the NAS journal.
- A manuscript is too broad or significant for a specialty journal but may not clear the Nature/Science exceptional-significance bar.
- An author wants to use the Direct Submission track and needs framing guidance.
- The author needs PNAS's scope boundaries, submission-track options, and desk-reject patterns before submitting.

## Scope & topic fit

- All natural sciences: biological, physical, chemical, earth, computational, mathematical, and social sciences meeting PNAS's significance standard.
- Research that makes a notable advance within a discipline and is interpretable — and worth knowing — to scientists in neighboring disciplines without specialist re-training.
- Work where the NAS-publishing prestige and broad readership are strategically valuable, e.g., definitive mechanism papers, landmark datasets, or integrative analyses.
- Interdisciplinary work bridging formal and natural sciences (e.g., physics-of-biology, computational social science, geobiology) where no single specialist journal is the obvious home.
- Clinical/translational work with clear mechanistic or public-health significance, provided it reaches beyond a clinical specialty audience.

## Method & evidence bar

- Methods must be complete and reproducible; PNAS requires a detailed Materials and Methods section (or equivalent) sufficient for independent replication.
- Data and code availability: PNAS requires explicit statements; deposition in recognized repositories is expected for genomic, structural, and large-scale quantitative data.
- Statistical reporting must include effect sizes, confidence intervals, and sample sizes; bare p-values are insufficient.
- For biological studies: reproducibility across replicates, appropriate controls, and clear statement of n throughout.
- For human-participant studies: ethics, consent, and registration are required; reporting-guideline compliance (CONSORT, STROBE, PRISMA) is expected.
- PNAS does not require a formal reporting summary in the Nature style, but statistical-methods transparency is closely scrutinized at review.

## Structure & house style

- PNAS publishes Research Articles, Letters (brief communications — re-check current terminology and length limits), and review-type articles; each has distinct format requirements — re-check which type fits the manuscript before submission.
- The Significance Statement is a mandatory plain-language paragraph for the non-specialist (re-check the current word limit): it is a primary triage and accessibility tool and should be drafted early, not added last.
- The abstract is unstructured and concise; like the Significance Statement, it must convey the advance to a broad audience.
- Main-text structure for Research Articles follows Introduction / Results / Discussion / Materials and Methods (full methods in main text, not SI); this is a distinguishing PNAS house rule.
- Supporting Information (SI) carries secondary validation, expanded datasets, and detailed protocols; SI figures and tables are numbered separately.
- References are formatted in PNAS style (re-check current citation style guide).

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "PNAS information for authors" and follow the current version at pnas.org.
- Re-check submission tracks: Direct Submission vs. any active track requiring member involvement (track rules have changed historically — verify current state).
- Re-check Significance Statement word limit, abstract format, article-type options, and word/figure limits per type.
- Re-check data/code/materials availability requirements, repository expectations (GenBank, PDB, GEO, etc.).
- Re-check ethics/consent/registration requirements, competing-interests disclosure, funding statement, and AI-use disclosure policy.
- Re-check SI formatting requirements and whether certain content categories must appear in main text vs. SI.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The Significance Statement is drafted in plain English, without jargon, and explains why a scientist outside the field should care.
- [ ] The Materials and Methods section is in the main text (not SI), complete enough for independent replication.
- [ ] The advance is positioned as meaningful to a discipline-level audience plus at least one adjacent field — not just a subfield specialty.
- [ ] Effect sizes, confidence intervals, and sample sizes are explicit throughout.
- [ ] Data/code deposition is confirmed; ethics/consent/registration documentation is ready.
- [ ] The correct submission track (Direct Submission or other) has been selected and the manuscript formatted accordingly.

## Common desk-reject triggers

- The Significance Statement reads as specialist jargon or merely restates the abstract — editors treat a weak Significance Statement as evidence of poor cross-disciplinary appeal.
- Materials and Methods placed entirely in SI rather than the main text, violating PNAS house rules.
- The advance is solid but confined to a sub-specialty with no clear message to adjacent fields — belongs in a discipline-specific journal.
- Statistics reported as bare p-values with no effect sizes or confidence intervals.
- The manuscript exceeds article-type length or figure limits without a justified exception.

## Re-routing decision

- Exceptional cross-disciplinary significance at Nature/Science level → `nature` or `science`.
- Broad multidisciplinary significance, open access preferred → `nature-communications` or `science-advances`.
- Solid disciplinary advance in cell/molecular biology with mechanistic depth → `cell`, `molecular-cell`, or relevant Nature portfolio journal.
- The paper is primarily a methods advance → `nature-methods` or a field-specific methods journal.
- Strong result from Chinese-led team with global multidisciplinary scope → `national-science-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Proceedings of the National Academy of Sciences
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the advance clear PNAS's discipline-plus-adjacent-field significance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission track / Significance Statement / article type / Methods placement / data-code / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
