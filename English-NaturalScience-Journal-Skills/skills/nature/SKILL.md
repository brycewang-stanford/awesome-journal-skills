---
name: nature
description: Use when targeting Nature or deciding whether a manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature (nature)

## Journal positioning

Nature is the world's most broadly read scientific weekly, published by Springer Nature. It publishes a tiny selection of primary research that represents a single, decisive conceptual or empirical advance of exceptional significance to scientists across disciplines — not just to specialists in the author's field. The readership spans biology, physics, chemistry, earth science, and beyond; every paper must therefore tell a compelling story to a scientifically literate non-specialist. Almost all manuscripts are desk-rejected by editors before reaching peer review because they do not clear the broad-significance bar.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature site and the submission system.

## When to trigger

- The author names Nature as the target venue.
- A manuscript represents a single, paradigm-shifting result and the author is deciding between Nature, Science, and Cell.
- A specialist paper needs radical re-framing into a one-sentence "why the world needs to know this now" advance.
- The author needs Nature's high-frequency desk-reject risks and credible alternative-venue routing before submitting.

## Scope & topic fit

- Any field of natural science or clinical science, provided the result is exceptional by cross-disciplinary standards — not just top-of-field.
- Fundamental discoveries that open new research directions (new mechanism, new phenomenon, new paradigm), rather than the best current increment in an ongoing program.
- Technology breakthroughs (AI systems, materials, therapeutics) where performance or principle crosses a conceptual threshold visible to scientists outside the field.
- Results that directly reshape scientific understanding of a major open question (origin of structures, disease mechanism, planetary science, evolution).
- Cross-disciplinary findings that bridge two or more fields and are best received by a joint audience.

## Method & evidence bar

- The central claim must be robustly supported and self-contained: controls, statistics, replication across conditions, and data quality must be unimpeachable, because Nature's post-publication scrutiny is intense.
- Reporting standards are strict: a Nature reporting summary (life sciences) covering statistics, randomization, blinding, sample sizes, and replication must accompany biological papers; equivalent rigor is expected in physical-science methods sections.
- Extended Data (up to 10 figures/tables) carries essential validation, freeing the main figures for the narrative advance.
- Data and code availability statements are mandatory; deposition in community-standard repositories is expected.
- For studies involving human participants: ethics approval, consent, pre-registration, and reporting-guideline compliance are required.

## Structure & house style

- Articles are short (main text is tightly constrained — re-check current word limits); the paper must make its conceptual contribution clear in the opening two paragraphs without assuming deep specialist knowledge.
- The title and abstract must convey the advance to a broad scientist: frame the finding ("We show that X causes Y") not the method ("We used CRISPR to ...").
- Letters (legacy format) and Articles both carry a brief Methods section in the main text; detailed protocols go into Supplementary Information or Extended Data, not the body.
- A significance statement or editor-facing cover letter must articulate in plain language why this result matters beyond the immediate field — editors use this as the first triage filter.
- Figures are publication-quality and must stand alone with legends; Nature is a print+online journal with tight figure-count limits (re-check current limits).
- Supplementary Information is for secondary validation; moving core results to the SI to meet length limits is a common desk-reject trigger.

## Official-submission checklist

- Search the live site for "Nature author instructions" and follow the current Springer Nature version.
- Re-check current article-type options (Article, Letter if still active, Brief Communication), word/figure limits, abstract format, and Extended Data allowance.
- Re-check reporting summary requirements (life-sciences checklist; physical/earth-sciences equivalents), data/code deposition policy, and materials-availability statement.
- Re-check preprint policy, embargo policy, AI-use disclosure, competing-interests and funding disclosure.
- Re-check ethics/consent/registration requirements for human or vertebrate-animal studies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence explaining why this result matters to scientists outside the immediate subfield — a biologist would ask "so what?" about a physics paper, and vice versa; that answer must be in paragraph one.
- [ ] The contribution is framed as a conceptual advance or new phenomenon, not as "the first study to use method X on system Y."
- [ ] The manuscript does not depend on prior field-specific jargon in the title, abstract, or opening paragraph.
- [ ] Extended Data carries all essential validation; the main figures tell the complete narrative with no gaps.
- [ ] Reporting summary, data/code availability, and ethics/consent documentation are complete before submission.
- [ ] The cover letter explicitly names the cross-disciplinary readership that will benefit.

## Common desk-reject triggers

- Significance is specialist-level only: "important advance in field X" without a compelling reason for a broader scientist to care.
- The paper is the fifth study of its kind rather than a decisive, paradigm-opening result.
- Core results buried in Supplementary Information; the main figures alone do not tell the story.
- Methods section is inadequate for reproducibility; no reporting summary or incomplete statistics reporting.
- Framing is technical ("we develop a method for ...") rather than discovery-based ("we discover that ...").
- A result that belongs in a Nature portfolio journal (nature-genetics, nature-methods, nature-materials, nature-medicine) — appropriate specialization is not a weakness.

## Re-routing decision

- Strong result, specialist framing or specialist audience → the appropriate Nature portfolio journal: `nature-genetics`, `nature-methods`, `nature-cell-biology`, `nature-materials`, `nature-medicine`, `nature-physics`, `nature-chemistry`, `nature-neuroscience`.
- Broad significance, AAAS context or US institutional framing → `science`.
- Solid, complete advance of broad-discipline interest, not exceptional → `nature-communications`, `science-advances`, or `pnas`.
- Cell-biology or molecular-mechanism advance with deep validation → `cell`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result clear the broad cross-disciplinary significance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / word limit / reporting summary / Extended Data / data-code / ethics / embargo>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
