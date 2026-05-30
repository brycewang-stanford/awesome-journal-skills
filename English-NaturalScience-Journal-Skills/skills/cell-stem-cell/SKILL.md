---
name: cell-stem-cell
description: Use when targeting Cell Stem Cell or deciding whether a stem-cell or regenerative-biology manuscript fits this Cell Press venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cell Stem Cell (cell-stem-cell)

## Journal positioning

Cell Stem Cell is the Cell Press flagship for stem-cell biology, regenerative medicine, and reprogramming. It publishes mechanistic studies in which stem or progenitor cells are the central biological unit — from pluripotency regulation and lineage specification through tissue-specific adult stem cells, organoids, and cellular reprogramming. The journal bridges fundamental developmental and cell biology with translational and therapeutic applications, but it demands mechanistic depth throughout: a paper that is primarily clinical or descriptive, without a molecular or cellular mechanism, does not fit. The readership spans developmental biologists, cell biologists, geneticists, and regenerative-medicine researchers; the advance must be legible and significant to this combined audience.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site.

## When to trigger

- The author names Cell Stem Cell as the target venue.
- A paper in stem-cell biology, reprogramming, or organoid biology needs the Cell Press flagship in the field.
- A mechanistic study of cell fate, lineage commitment, or tissue regeneration has both molecular depth and in vivo relevance and the author is choosing between Cell Stem Cell, `cell`, and `developmental-cell`.
- The author needs Cell Stem Cell's specific evidence bar (mechanism + in vivo requirement), STAR Methods obligations, and desk-reject patterns before submitting.

## Scope & topic fit

- Pluripotency: mechanisms of pluripotent stem-cell (PSC) maintenance, exit, and re-entry; transcription-factor networks, epigenetic regulation, and signaling in ESCs and iPSCs.
- Cellular reprogramming: direct reprogramming of somatic cells, transdifferentiation, and mechanistic understanding of the barriers and determinants.
- Lineage specification and organogenesis: specification of tissue progenitors from PSCs or in vivo, with mechanistic insight into the decision points.
- Adult stem cells: identity, niche interactions, self-renewal vs. differentiation decisions, and their regulation in homeostasis and regeneration.
- Organoids and advanced stem-cell models: only when the model is used to answer a mechanistic question or validate a therapeutic concept — technology development alone is insufficient.
- Translational and disease applications: disease modeling with iPSCs, gene-correction approaches, or cell-therapy strategies — but always with a mechanistic underpinning that goes beyond the clinical observation.
- Aging and stem-cell dysfunction: mechanisms by which stem-cell activity declines or becomes aberrant with age or disease.

## Method & evidence bar

- Mechanism plus in vivo relevance is the standard combination: a purely in vitro mechanistic study must have compelling reason why in vivo validation cannot or need not be done; most papers require at least one in vivo or ex vivo component.
- For PSC/reprogramming papers: multiple independent cell lines, rigorous pluripotency authentication (teratoma, chimera, or equivalent), and appropriate passage-number controls.
- For adult stem-cell papers: lineage tracing or clonal analysis in vivo is often required to demonstrate stem-cell identity and behavior; FACS isolation with validated markers is the minimum.
- STAR Methods is mandatory: complete experimental details, Key Resources Table (all antibodies, cell lines, mouse strains, plasmids, software with identifiers/RRIDs), and data/code availability at initial submission.
- For sequencing or omics data: deposition in GEO, SRA, or equivalent; accession numbers before acceptance.
- Statistics must distinguish biological from technical replicates, report effect sizes, and specify tests throughout.
- For human iPSC work: donor consent and ethics approval are required; for any human embryo or hESC work, re-check current ethical compliance requirements carefully.

## Structure & house style

- Cell Stem Cell publishes Articles, Short Reports (re-check current types and length limits), and occasionally Resource papers; the standard mechanistic paper is an Article.
- STAR Methods is appended after main references with defined subheadings and the Key Resources Table; it must be complete at initial submission.
- Figures must build the mechanistic argument in stages; a model figure at the end of the main figures is standard, depicting the proposed molecular/cellular mechanism.
- Graphical abstracts and eTOC blurbs are required or strongly expected — re-check current Cell Press format and resolution requirements.
- Supplemental information carries secondary validations, extended characterization of additional cell lines, and supporting datasets — not core evidence.
- The Discussion must clearly delineate translational implications where relevant, but without over-claiming therapeutic readiness.

## Official-submission checklist

- Search the live site for "Cell Stem Cell author instructions" and follow the current Cell Press version.
- Re-check article types, word and figure limits per type, and abstract format.
- Re-check STAR Methods requirements: Key Resources Table format, RRID requirements, reagent and cell-line identification standards.
- Re-check sequencing/omics data deposition requirements (GEO, SRA) and accession-number submission timeline.
- Re-check ethics requirements for human iPSC/ESC work, human embryo research, and patient-derived samples — this area has jurisdiction-specific regulations that change; re-check the current Cell Press ethics policy carefully.
- Re-check graphical abstract format, eTOC blurb length, competing-interests and funding disclosure, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The paper is mechanistic at the level of the stem or progenitor cell: a cellular or molecular mechanism is resolved, not just described.
- [ ] In vivo relevance is demonstrated (lineage tracing, transplantation, or animal model) or a compelling exception is justified.
- [ ] STAR Methods is complete, including Key Resources Table with RRIDs for all antibodies, cell lines, and mouse strains.
- [ ] PSC lines are authenticated by appropriate assay; adult stem-cell identity is validated by lineage tracing or equivalent.
- [ ] Ethics documentation for human cell sources is confirmed; consent and IRB approvals are in place.
- [ ] Sequencing data accession numbers are confirmed or in process; graphical abstract is drafted.

## Common desk-reject triggers

- Descriptive characterization of stem-cell behavior without a mechanism: showing that a factor affects differentiation is not sufficient — how and why must be mechanistically addressed.
- STAR Methods is absent or the Key Resources Table is missing cell-line and antibody identifiers — Cell Press editors check this at intake.
- In vitro-only mechanistic study for a question where in vivo validation is feasible and expected by the field.
- An organoid or iPSC technology paper where the technology is the contribution and no mechanistic or disease question is answered — technology-development papers need an application driving a discovery.
- The paper is a clinical trial or cohort study without a mechanistic stem-cell component — that paper belongs in a clinical or translational journal.
- Missing graphical abstract or eTOC blurb at submission.

## Re-routing decision

- The mechanistic advance is at Cell-level conceptual significance and the biology extends beyond stem cells → `cell`.
- Developmental mechanism broader than adult stem cells and in vivo, not requiring PSC context → `developmental-cell`.
- The advance is in cell biology broadly, not specifically stem/progenitor cells → `nature-cell-biology`.
- Mechanistic molecular biology at biochemical/structural depth underlying a stem-cell process → `molecular-cell`.
- Solid stem-cell advance below Cell Stem Cell's mechanistic depth → `the-embo-journal`, `plos-biology`, or a specialist developmental journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cell Stem Cell
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there a mechanistic advance with in vivo relevance and STAR Methods-ready documentation?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <STAR Methods / Key Resources Table / PSC authentication / ethics/consent / data deposition / graphical abstract>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
