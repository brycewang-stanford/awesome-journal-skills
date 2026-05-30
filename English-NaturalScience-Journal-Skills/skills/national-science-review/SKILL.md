---
name: national-science-review
description: Use when targeting National Science Review (NSR) or deciding whether a multidisciplinary manuscript fits China's flagship broad-science journal (OUP/CAS). Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# National Science Review (national-science-review)

## Journal positioning

National Science Review is China's flagship multidisciplinary scientific journal, published by Oxford University Press on behalf of the Chinese Academy of Sciences. It publishes primary research, reviews, and perspectives across the natural sciences — physics, chemistry, materials, life sciences, earth/environmental science, and engineering — with a particular strength in areas where Chinese research leads globally. NSR occupies a distinctive dual role: it is an internationally peer-reviewed research journal and a venue for authoritative synthetic reviews of fields in which China-based science is making transformative contributions. The readership is global but the editorial perspective explicitly showcases the best of Chinese science alongside internationally sourced excellence.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the OUP/NSR site.

## When to trigger

- The author names National Science Review (or NSR) as the target venue.
- A manuscript from a Chinese institution seeks the highest-visibility broad-science venue that simultaneously serves domestic and international audiences.
- A paper has been rejected from Nature or Science and has significant scope but does not fit a Nature portfolio journal's narrower remit.
- An invited or spontaneous synthetic review covers a field in which China-based research has distinctive depth.
- The author is navigating between NSR, `the-innovation`, `pnas`, `nature-communications`, and `science-advances`.

## Scope & topic fit

- Physical sciences: condensed matter, quantum science, photonics, new materials, advanced manufacturing — areas of established Chinese research leadership.
- Life sciences: structural biology, genomics, neuroscience, biomedical engineering — where the advance is of international significance and complete in mechanism.
- Earth, environmental, and climate science: global-significance findings, especially those leveraging Chinese observation infrastructure or modeling capacity.
- Energy, sustainability, and materials-for-energy — a growing strategic emphasis in NSR's portfolio.
- Synthetic reviews: authoritative reviews of rapidly advancing fields where the review team can speak from inside active research programs, not as external summarizers.
- Cross-disciplinary breakthroughs that do not fit a narrow-specialty journal but are not of exceptional significance for Nature/Science.

## Method & evidence bar

- Primary research must meet international peer-review standards for the relevant discipline: rigorous controls, appropriate statistics with effect sizes, adequate replication, and complete methodology.
- Data and code availability are expected; deposition in recognized repositories (CSTR, NCBI, PDB, CCDC, etc.) is appropriate and increasingly required.
- For life-sciences studies involving human participants: ethics, consent, and registration are required; relevant reporting guidelines apply.
- Reviews must be comprehensive and authoritative, not descriptive surveys; the review team should have primary research contributions in the area reviewed.
- NSR publishes several article types — Research Articles, Reviews, Perspectives, Briefs, Letters (re-check current type list); the method bar varies by type but rigor is uniformly expected.

## Structure & house style

- Research Articles have a standard structure with an Abstract, Introduction, Results, Discussion, and Methods; review articles are typically longer with clear section organization and a forward-looking synthesis.
- Abstracts are concise and unstructured; they should be accessible to a broad cross-disciplinary audience within the natural sciences — not specialist-only.
- NSR encourages authors to frame the advance in terms of the field's global trajectory, with explicit positioning against recent international work, not only against China-based literature.
- Perspectives and Letters are shorter and opinion-forward; they are suitable for rapid framing of emerging results or field developments.
- The journal expects high-quality figures that are publication-ready and accessible; figure legends should be self-sufficient.
- References should include both international foundational works and current Chinese-laboratory contributions where these are genuinely relevant.

## Official-submission checklist

- Search the live site for "National Science Review author instructions" (OUP site) and follow the current version.
- Re-check article types available, word and figure limits per type, and abstract format requirements.
- Re-check data/code/materials availability requirements and any field-specific repository expectations.
- Re-check ethics/consent/registration requirements for human or animal research.
- Re-check open-access options, APC and licensing policy — NSR offers both subscription and open-access publishing.
- Re-check competing-interests, funding disclosure, and AI-use disclosure policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The advance is of international significance and the manuscript frames it relative to global state-of-the-art, not only against Chinese-literature context.
- [ ] The article type is appropriate: primary discovery goes in Research Article, not disguised as a Perspective.
- [ ] Statistics and methodology meet international standards for the relevant discipline; effect sizes and confidence intervals are reported.
- [ ] For reviews: the team has primary expertise in the area; the synthesis is forward-looking and not merely descriptive.
- [ ] Data/code are deposited or an availability statement is prepared; ethics/consent documentation is ready.
- [ ] The abstract reads clearly to a physicist, chemist, or biologist outside the immediate subfield.

## Common desk-reject triggers

- Significance is narrowly disciplinary with no message to the broad NSR audience across physics, chemistry, and biology.
- A review article that summarizes without synthesis — NSR reviews must offer expert perspective on where the field is going, not just where it has been.
- Methodology that does not meet international standards for the relevant field; peer reviewers are drawn from the global community.
- The paper is purely technical or engineering-focused without a scientific discovery component visible to a natural-science audience.
- Poor international framing — a paper that reads only as a Chinese institutional report rather than as a contribution to global science.

## Re-routing decision

- Exceptional significance for a global cross-disciplinary audience → `nature`, `science`, or `pnas`.
- Broad multidisciplinary open access, Springer Nature brand → `nature-communications`.
- AAAS open-access multidisciplinary → `science-advances`.
- Cross-disciplinary innovation with Cell Press partnership, fast, global → `the-innovation`.
- Field is narrowly life-science/cell-biology → `cell`, `molecular-cell`, or a Nature portfolio life-science journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] National Science Review
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the advance meet international standards and have cross-disciplinary natural-science significance?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / word limit / data-code / OA option / ethics / review team expertise>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
