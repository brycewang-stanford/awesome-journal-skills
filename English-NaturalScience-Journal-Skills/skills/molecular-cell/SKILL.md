---
name: molecular-cell
description: Use when targeting Molecular Cell (Mol Cell) or deciding whether a molecular-biology manuscript fits this Cell Press venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Molecular Cell (molecular-cell)

## Journal positioning

Molecular Cell is a Cell Press flagship for molecular biology at its most mechanistic, operating at the interface of biochemistry, structural biology, and molecular genetics. Where Cell publishes conceptual leaps at the level of cell biology broadly, Molecular Cell demands resolution at the level of the molecule: how exactly does the protein, RNA, or complex work, and what is the structural or biochemical basis? The readership is the global molecular-biology and biochemistry community — scientists who evaluate papers by asking whether the mechanistic logic is airtight and the molecular evidence is definitive. Molecular Cell is narrower than Cell in scope but deeper in expectation: a paper acceptable at Mol Cell must resolve a molecular mechanism at a depth that could not be published without the biochemical or structural data.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site.

## When to trigger

- The author names Molecular Cell (or Mol Cell) as the target venue.
- A mechanistic molecular-biology paper has structural, biochemical, or single-molecule resolution and the author is choosing between Molecular Cell, `cell`, and `nature-structural-and-molecular-biology`.
- A paper resolves the mechanism of a known but poorly understood molecular process (transcription, translation, splicing, DNA repair, ubiquitin pathway, condensate formation) and needs Mol Cell-specific framing.
- The author needs Mol Cell's evidence bar, STAR Methods requirements, and desk-reject patterns before submitting.

## Scope & topic fit

- Transcription, co-transcriptional processing, RNA splicing, and RNA-protein interactions at mechanistic resolution.
- DNA replication, repair, recombination, and genome stability mechanisms.
- Translation, ribosome biology, and protein quality control.
- Chromatin biology, epigenetic regulation, and 3D genome organization — where the molecular mechanism is resolved, not just described.
- Protein-complex assembly, post-translational modification cascades, and ubiquitin-proteasome system mechanisms.
- Biomolecular condensates and phase-separation biology at mechanistic and structural resolution.
- Single-molecule biophysics, cryo-EM, cryo-ET, and structural biochemistry when the structure directly resolves a mechanistic question — not structure for structure's sake.

## Method & evidence bar

- The molecular mechanism must be resolved, not inferred: biochemical reconstitution, single-molecule experiments, high-resolution structural data, or quantitative kinetic measurements are expected for the central mechanistic claims.
- STAR Methods is mandatory: all experimental details, reagent lists with identifiers (Key Resources Table), and data/code availability in the standardized Cell Press STAR Methods format.
- For structural studies: coordinate and map deposition (PDB, EMDB) with accession numbers before acceptance.
- For sequencing or omics data: deposition in GEO, SRA, or equivalent; accession numbers before acceptance.
- In vivo or cell-based validation is expected alongside in vitro reconstitution: Mol Cell papers characteristically combine biochemistry (telling you how) with cell-based or genetic experiments (telling you that it matters).
- Statistics must specify tests, n values (distinguishing technical from biological replicates), and effect sizes throughout.

## Structure & house style

- Molecular Cell publishes Articles and shorter Reports (re-check current article types and length limits); the standard mechanistic paper is an Article.
- STAR Methods is appended after main references, with defined subheadings and the Key Resources Table; it must be complete at initial submission.
- The main text builds the mechanistic argument figure by figure; each figure advances the mechanism by one logic step, and the final figure typically provides the integrative model.
- A model figure (schematic of the proposed mechanism) is nearly universal at Mol Cell and is expected at the conclusion of the main figures.
- Graphical abstracts and eTOC blurbs are required or strongly expected — re-check current Cell Press requirements.
- Supplemental information carries extended biochemical characterization, additional genetic backgrounds, and secondary validations but should not be required to understand the central mechanistic argument.

## Official-submission checklist

- Search the live site for "Molecular Cell author instructions" and follow the current Cell Press version.
- Re-check article types, word and figure limits per type, and abstract format.
- Re-check STAR Methods requirements: Key Resources Table format, subheading conventions, and reagent-identifier requirements (RRIDs).
- Re-check structural data deposition (PDB, EMDB), sequencing data deposition (GEO, SRA), and accession-number requirements.
- Re-check graphical abstract requirements, competing-interests disclosure, funding statement, and AI-use disclosure policy.
- Re-check ethics/consent requirements for any human-derived material or patient samples.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The mechanistic conclusion is stated in one sentence — not as a correlation or phenotype, but as a specific molecular event: "Protein X remodels complex Y by inserting helix Z into interface W."
- [ ] STAR Methods is fully drafted with all reagents, constructs, antibodies, and software listed in the Key Resources Table with identifiers.
- [ ] In vitro reconstitution and cell-based validation (or structural and genetic data) both support the central mechanistic claim.
- [ ] A mechanistic model figure (schematic) is drafted and ready as the final or penultimate main figure.
- [ ] Structural coordinates or sequencing data accession numbers are confirmed or in process.
- [ ] The Discussion distinguishes the proposed mechanism from competing models in the recent literature.

## Common desk-reject triggers

- The paper characterizes a molecular phenotype (e.g., a protein affects transcription) without identifying the molecular mechanism (how, step by step, at molecular resolution).
- STAR Methods is absent or incomplete — Mol Cell editors check this at intake, as for all Cell Press journals.
- Structure-only paper with no functional or mechanistic payoff: elegant cryo-EM without biochemical or genetic validation of the mechanistic inference belongs in a structural-biology journal.
- The scope is Cell-level broad (whole-organism, disease model, clinical relevance is the main contribution) rather than Mol Cell-level deep — that paper belongs in `cell` or a disease-focused journal.
- The paper is a solid mechanistic advance but falls short of resolving the core mechanistic controversy; reviewers expect definitive, not suggestive.
- Missing graphical abstract or eTOC blurb at submission.

## Re-routing decision

- Conceptual-leap significance extending beyond molecular biology into cell biology broadly → `cell`.
- Structure-function mechanism at highest structural resolution with limited cell-biology context → `nature-structural-and-molecular-biology`.
- Exceptional significance for a cross-disciplinary science audience → `nature` or `science`.
- Solid mechanistic molecular-biology advance below Mol Cell's resolution/depth bar → `the-embo-journal` or `nucleic-acids-research` (for nucleic-acid biology).
- Stem-cell or regeneration context with molecular mechanism → `cell-stem-cell`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Molecular Cell
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the molecular mechanism resolved at biochemical/structural resolution with in vivo validation?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <STAR Methods / Key Resources Table / structural/sequencing deposition / graphical abstract / article type>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
