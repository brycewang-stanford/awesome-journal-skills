---
name: science-advances
description: Use when targeting Science Advances (Sci Adv) or deciding whether a multidisciplinary open-access manuscript fits this AAAS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science Advances (science-advances)

## Journal positioning

Science Advances is the AAAS open-access multidisciplinary journal, launched as a sister to Science. It publishes significant advances across the sciences — broader in scope and lower in the significance bar than Science itself, but demanding more than the typical disciplinary society journal. The AAAS family framing means the editorial culture values cross-disciplinary reach, methodological rigor, and clear societal or scientific relevance. Science Advances is the natural destination for solid, important work that falls just below Science's exceptional-significance threshold or for papers where open-access publishing is a mandate. Its breadth across natural science, social science, and engineering makes it unusual among open-access multidisciplinary venues.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAAS / Science Advances site.

## When to trigger

- The author names Science Advances as the target venue.
- A manuscript has been considered at Science and needs re-routing within the AAAS family.
- An open-access mandate applies and the author wants an AAAS-brand multidisciplinary home.
- The author needs to distinguish Science Advances from Nature Communications and PNAS for venue selection.

## Scope & topic fit

- Natural sciences across all disciplines: biology, chemistry, physics, earth/environmental, materials, engineering, and computational science.
- Social and behavioral sciences when the methodology meets natural-science rigor standards — a genuine AAAS breadth distinguishing Sci Adv from many competitors.
- Applied and translational advances (new materials, biomedical devices, computational tools) with demonstrated significance beyond the immediate application.
- Cross-disciplinary research where multiple methodologies combine to address a significant question — AAAS's interdisciplinary culture is an advantage for these papers.
- Environmental, sustainability, and global-health science where societal relevance is explicit.

## Method & evidence bar

- The advance must be technically rigorous and reproducible: methods must be described in full, statistics must include effect sizes and confidence intervals, and controls must be adequate by field standards.
- Data and code availability: AAAS requires explicit statements; community-standard deposition (GenBank, GEO, Zenodo, GitHub, etc.) is expected.
- For human-participant research: ethics approval, consent, registration, and reporting-guideline compliance are required.
- The bar is higher than a typical society journal for significance but broader than Science in scope: a complete, rigorous study that moves a field is publishable even if it does not move all of science.
- Supplementary Materials carry secondary validation; the main text must be self-contained for the core claim.

## Structure & house style

- Science Advances publishes Research Articles and, re-check current article types, shorter formats if available. Research Articles are the main format.
- The abstract is structured (check current required sub-headings — historically: one paragraph with statement of advance prominent). Re-check current abstract format requirements.
- Supplementary Materials accompany the main paper; figures/tables therein are numbered separately.
- The manuscript should open with a brief, accessible framing of the scientific problem and state the advance clearly in the introduction — AAAS readers span fields.
- Unlike Science, there is no strict word minimum that forces brevity: papers can be complete, but padding is not rewarded.
- A clear statement of significance — either in the abstract or cover letter — that articulates cross-disciplinary relevance is important for triage.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Science Advances author instructions" and follow the current AAAS version.
- Re-check article types, abstract format, word and figure limits, and Supplementary Materials policy.
- Re-check data/code/materials availability requirements and community repository expectations.
- Re-check open-access licensing (Science Advances is fully OA — re-check Creative Commons license options and any APC waiver policies).
- Re-check ethics/consent/registration requirements, competing-interests and funding disclosure, AI-use disclosure, and preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The advance is genuinely significant within its discipline and has a clear message to adjacent fields or to a policy/societal audience.
- [ ] The paper is framed as a result rather than as a methods report, unless the method itself is the discovery.
- [ ] Supplementary Materials carry validation only; the main text is self-contained for evaluating the central claim.
- [ ] Data/code deposition is complete; ethics/consent/registration is confirmed.
- [ ] The abstract and cover letter explicitly position the advance relative to current literature without requiring specialist knowledge to understand the "so what."
- [ ] Open-access licensing requirements have been verified with funder/institution OA policies.

## Common desk-reject triggers

- The advance is solid but entirely within a narrow sub-specialty without any cross-disciplinary framing — better placed in the relevant specialty journal.
- The paper is a technical methods note with no primary scientific discovery; even a strong new tool needs a biological or physical application demonstrating significance.
- Supplementary Materials carry the most important evidence and the main text is incomplete as a standalone document.
- Reporting is incomplete: missing effect sizes, sample sizes, or ethical approvals for human/animal work.
- The paper's framing assumes AAAS-style cross-disciplinary appeal but the introduction is opaque to scientists outside one sub-specialty.

## Re-routing decision

- The result clears Nature/Science-level significance → `science` or `nature`.
- Open-access multidisciplinary, Springer Nature brand preferred → `nature-communications`.
- Broad multidisciplinary, NAS-published, prefers structured Methods in main text → `pnas`.
- AAAS cell/molecular biology mechanistic advance with full validation → `cell` (if significance and depth warrant).
- Chinese-flagship multidisciplinary, open-access framing → `the-innovation` or `national-science-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science Advances
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the advance clear the AAAS significance bar above a specialty-journal level?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / abstract format / data-code / OA license / ethics / Supplementary policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
