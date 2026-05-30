---
name: chem
description: Use when targeting Chem (Cell Press) or deciding whether a chemistry manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Chem (chem)

## Journal positioning

Chem is the Cell Press flagship chemistry journal, publishing fundamental chemical discoveries that address big problems — sustainability, energy, medicine, materials — rather than incremental advances within a subfield. The readership spans all of chemistry and expects a paper to matter to someone working in a different area of chemistry or at the chemistry-biology/physics interface. Chem explicitly rewards work that connects chemical insight to large-scale societal or scientific challenges. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press / Chem site and submission system.

## When to trigger

- The author names Chem or the Cell Press chemistry portfolio as the target venue.
- A chemistry manuscript has clear broad significance and a connection to sustainability, energy, catalysis, or medicine but needs re-framing away from subfield-specialist language.
- A study is too conceptually broad for JACS or Angew Chem and needs a venue that rewards cross-disciplinary impact.
- The author needs Chem's desk-reject risks, editorial DNA, and alternative-venue guidance before submitting.

## Scope & topic fit

- Fundamental chemical discoveries with demonstrable real-world relevance: catalysis solving efficiency/selectivity problems with sustainability implications; materials with designed structure-property function for energy or medicine.
- Chemical biology bridging molecular mechanism to biological function or therapeutic relevance, not incremental ligand optimization.
- Synthesis enabling previously inaccessible molecular complexity with clear application rationale, not trophy synthesis alone.
- Chemical theory/computation that reveals a new mechanistic principle testable in experiment, not standalone numerical benchmarking.
- Energy/sustainability chemistry: CO₂ conversion, nitrogen fixation, water splitting — but results must be contextualized against real-world performance metrics (stability, scalability, cost trajectory), not just peak efficiency.
- Supramolecular, polymer, or soft-matter chemistry when the design principle is conceptually new and function-relevant.

## Method & evidence bar

- Novelty must be conceptual, not incremental: a new reaction class, a new mechanistic understanding, a new design principle — not a 2% yield improvement on a known transformation.
- Mechanism must be established, not inferred: kinetics, spectroscopic or computational evidence, isotope labeling, or crystallographic data as appropriate.
- Stability, reusability, and scalability data are expected when the work is framed as relevant to applications; a single-cycle or thin-film result that ignores bulk performance is insufficient.
- Computational work must be validated against experimental observables; stand-alone DFT data without experimental corroboration require exceptional justification.
- Cross-disciplinary claims (e.g., biological activity, device performance) must meet the methodological standard of the receiving field, not just the chemist's standard.
- STAR Methods is the Cell Press format for full methods; reviewers will check reproducibility in detail.

## Structure & house style

- The opening paragraph of the introduction must state the big problem, why current chemical approaches fall short, and precisely what conceptual advance this paper makes — not a literature survey.
- Cell Press uses a structured format: main text, STAR Methods, and supplementary information; the significance/contribution framing follows the Cell Press "In Brief" and "Highlights" convention.
- Figures should tell the scientific story without the text: figure panels should build from concept to mechanism to performance, with clear axis labels and appropriate controls visible in the figure itself.
- Graphical abstract is mandatory; it must accurately represent the conceptual advance, not just illustrate a molecule.
- The discussion should connect results back to the big-picture problem and to outstanding open questions, not merely recapitulate the data.
- Re-check current article-type options (Article vs. Report vs. Preview) and length limits on the live author guide.

## Official-submission checklist

- Search the live site for "Chem author instructions" or "Cell Press author guidelines" and follow the current version.
- Re-check article-type definitions, length limits, figure-count limits, STAR Methods requirements, and supplemental information scope.
- Re-check graphical abstract format specs, "In Brief" and "Highlights" word limits, and the significance statement requirement.
- Confirm data/code availability policy, deposition requirements for crystallographic or sequence data, and any reporting-checklist requirements for biological assays.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what fundamental chemical principle this paper establishes and why it matters beyond synthetic chemistry.
- [ ] The contribution is framed as a conceptual/mechanistic advance, not as "first synthesis of" or "highest reported yield."
- [ ] The big-picture problem (sustainability, energy, medicine, or another cross-disciplinary challenge) is explicitly connected to the chemical results in the introduction and discussion.
- [ ] Mechanism is established by direct evidence, not inferred from product distribution alone.
- [ ] STAR Methods is complete, figures are self-explanatory, and graphical abstract is accurate.
- [ ] Application-relevant data (stability, scalability, real-world metrics) are included where the framing invokes practical significance.

## Common desk-reject triggers

- Scope too narrow: a new ligand class for a known transformation with no evidence of broader significance or novel mechanistic insight.
- "First synthesis" or "record yield" framing without connecting the achievement to a conceptual principle or unsolved problem.
- Application claims (e.g., photocatalysis, drug activity) supported only by proof-of-concept data, ignoring stability, selectivity, or real-world operating conditions.
- Computational study with no experimental validation and no mechanistic principle that could not have been inferred from existing theory.
- Writing framed for an audience of specialists in a narrow subfield, with no attempt to establish significance for the broader chemistry readership.

## Re-routing decision

- Conceptually excellent chemistry without the broad-problem framing → `nature-chemistry` (also highly selective, but scope can be more fundamental/curiosity-driven) or `journal-of-the-american-chemical-society`.
- Catalysis advance where mechanism and significance are strong → `nature-catalysis`.
- Materials-oriented chemistry with structure-property depth → `nature-materials` or `advanced-materials`.
- Energy/sustainability chemistry that meets quantitative performance standards → `joule` or `energy-and-environmental-science`.
- Nanoscience aspect dominant → `acs-nano` or `nature-nanotechnology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Chem (Cell Press)
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the chemistry establish a new conceptual principle with mechanistic evidence and real-world contextualization?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / STAR Methods / graphical abstract / highlights / data deposition / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
