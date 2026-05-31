---
name: nature-chemistry
description: Use when targeting Nature Chemistry (Nat Chem) or deciding whether a chemistry manuscript fits this Springer Nature venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Chemistry (nature-chemistry)

## Journal positioning

Nature Chemistry is a Springer Nature journal that publishes research and review content of exceptional significance across the full breadth of chemistry, with an explicit editorial mandate to attract readers from all areas of chemistry and from adjacent disciplines. The defining criterion is not just novelty within a sub-field but conceptual reach: a Nature Chemistry paper changes how chemists think about a problem, introduces a genuinely new paradigm, or connects chemistry to broader scientific questions in a compelling way. The journal also publishes News & Views, perspective articles, and Reviews; the tone throughout is narrative and accessible, unlike a specialist technical journal.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature submission portal.

## When to trigger

- The author names Nature Chemistry or Nat Chem as the target venue.
- A chemistry manuscript has a conceptual advance that reframes a problem or opens a new direction, and the author is evaluating it against `journal-of-the-american-chemical-society`, `angewandte-chemie-international-edition`, and nature-chemistry.
- A paper's significance can be explained to chemists outside the originating sub-field in a few compelling sentences.
- The author needs Nature Chemistry's desk-reject risks and alternative-venue guidance.

## Scope & topic fit

- Chemistry that solves or reframes a fundamental problem: new bond-forming logics, unexpected reaction mechanisms, or chemical architectures with conceptual implications.
- Chemical biology where the chemistry itself is the advance: new modes of reactivity with biomolecules, chemical probes that reveal new biology.
- Physical and theoretical chemistry results that change how a phenomenon is understood, not only how it is calculated.
- Supramolecular and systems chemistry where emergent behaviour is mechanistically explained.
- Interdisciplinary results that make chemistry the engine of a broader scientific advance (materials, energy, medicine) — but the chemistry must be the intellectual core.

## Method & evidence bar

- The result must pass a "would a chemist in any sub-field find this remarkable?" test; significance within the originating sub-field is necessary but not sufficient.
- Mechanistic completeness is expected: conceptual claims must be supported by direct experimental evidence; elegantly designed experiments are valued over exhaustive cataloguing.
- Computational work that changes conceptual understanding is welcome, but results must be experimentally validated or directly predictive.
- Data quality, reproducibility, and characterisation meet the same standard as JACS/ACIE; the narrative is elevated but the science is not softer.
- A Nature-family reporting summary is required; re-check the current checklist.

## Structure & house style

- The article opens with a narrative paragraph accessible to any chemist: the unsolved problem, why it matters, and what the paper delivers — without sub-field jargon in the first sentence.
- The Results and Discussion section is often unified into a narrative flow rather than a rigidly subdivided experimental catalogue.
- Methods are placed after the main text (or in SI); detailed experimental procedures are in the SI.
- Nature Chemistry publishes Articles (longer, full mechanistic story) and, less commonly, Letters (shorter, urgent conceptual advance); re-check the current article-type definitions.
- Extended Data figures are available for supporting experiments that belong in the narrative flow but would crowd the main figures.
- A graphical/visual abstract is required; re-check current specifications.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Chemistry author information" and follow the current Springer Nature version.
- Re-check article type (Article vs. Letter), current length limits for main text and abstract, and maximum figure count.
- Confirm Extended Data figure policy, reporting summary requirements, and data/code availability statement.
- Verify author-contribution statement, competing-interests, AI-use disclosure, and preprint/embargo policy.
- Re-check open-access options and APC structure.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence explaining why any chemist — not just a specialist — would find this result remarkable.
- [ ] The opening paragraph tells the conceptual story without sub-field jargon; a physical chemist can follow an organic chemistry paper and vice versa.
- [ ] The mechanism is established by direct evidence, not inferred from product distribution alone.
- [ ] Extended Data figures are used for supporting experiments; the main figures carry the narrative.
- [ ] Reporting summary, data/code availability, and author contributions are complete.

## Common desk-reject triggers

- A result that is highly significant within a sub-field but whose conceptual implications cannot be explained to the rest of chemistry without a glossary.
- A "new reaction / new compound" paper framed as novelty-within-a-class rather than as a conceptual advance.
- Mechanistic proposals without supporting experimental evidence (isotope effects, kinetics, spectroscopy, computation).
- A paper that belongs in a specialist journal (e.g., a comprehensive synthetic methodology study without broader conceptual framing) sent to Nature Chemistry for prestige rather than fit.
- Missing or inadequate reporting summary or data availability statement.

## Re-routing decision

- Conceptual advance in chemistry but the work is comprehensive/methodological rather than single-concept → `journal-of-the-american-chemical-society` or `angewandte-chemie-international-edition`.
- Catalysis-centric conceptual advance with mechanism and significance → `nature-catalysis`.
- The advance is broadly scientific (not chemistry-centric) → Nature, Science, or the relevant Nature-portfolio sub-journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Chemistry
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result constitute a cross-sub-field conceptual advance with mechanistic support?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / Extended Data / reporting summary / data-code / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
