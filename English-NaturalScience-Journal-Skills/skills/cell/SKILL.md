---
name: cell
description: Use when targeting Cell (Cell Press) or deciding whether a cell/molecular-biology manuscript fits this flagship venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cell (cell)

## Journal positioning

Cell is the Cell Press flagship and one of the most prestigious journals in life science, publishing conceptually transformative papers in cell and molecular biology, systems biology, genetics, and adjacent fields where the cell or molecule is the unit of discovery. Cell is not a general biology journal: it demands a complete, mechanistic molecular story validated to a depth that stands as the field's new benchmark. The readership is the global cell and molecular biology community, including scientists in adjacent disciplines (structural biology, immunology, neuroscience, cancer biology, microbiology) when the mechanistic insight has field-wide implications. An editorial triage is strict; editors look for papers that reframe how the field thinks, not just papers that add to an ongoing mechanistic program.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site.

## When to trigger

- The author names Cell as the target venue.
- A mechanistic molecular-biology paper has deep validation and represents a conceptual leap, and the author is choosing among Cell, `molecular-cell`, `nature-cell-biology`, or `nature`.
- A paper proposes a new mechanistic framework (signaling pathway, gene-regulatory circuit, structural mechanism) and needs Cell-specific framing guidance.
- The author needs Cell's method-and-evidence bar, STAR Methods requirements, and desk-reject heuristics before submitting.

## Scope & topic fit

- Cell and molecular biology: signaling, gene regulation, chromatin, RNA biology, protein homeostasis, cell cycle, cell death — provided the mechanism has implications that extend beyond the specific system studied.
- Systems biology and multi-omic approaches where the integration produces a mechanistic insight, not just a catalogue.
- Structural biology with a direct mechanistic and functional payoff: structure for structure's sake belongs elsewhere.
- Genetics and genomics: GWAS-to-mechanism stories, not population-scale association studies alone.
- Cancer, immunology, neuroscience, and developmental biology papers where the unit of discovery is the molecular or cellular mechanism — if the primary contribution is clinical, the routing changes.
- New methodologies (CRISPR screens, single-cell platforms, imaging approaches) when the method is demonstrated to produce a biological discovery of Cell-level significance.

## Method & evidence bar

- The complete mechanistic story is the non-negotiable standard: Cell does not publish descriptive "-omics" surveys; every association must be mechanistically validated.
- Deep validation is required: in vitro and in vivo data where relevant; multiple orthogonal approaches confirming the key mechanistic step; loss-of-function and gain-of-function; rescue experiments.
- STAR Methods (Structured, Transparent, Accessible Reporting) is mandatory: all methods, reagent lists (key resources table), and data/code availability must be provided in the standardized STAR Methods format at the time of initial submission.
- Statistics: the paper must specify statistical tests, n values, and whether data represent technical or biological replicates; effect sizes and confidence intervals should be reported.
- Data deposition: raw data, processed datasets (sequencing, proteomics, structural coordinates), and code must be deposited in appropriate repositories with accession numbers provided before acceptance.
- For human-participant work: ethics, consent, and relevant reporting guidelines apply.

## Structure & house style

- Cell publishes Articles (standard long-form) and shorter Resource papers (re-check current types); the format for a standard mechanistic paper is the full Article.
- STAR Methods is a standalone, structured section appended after the main references: it contains all experimental details organized under defined subheadings, plus a Key Resources Table listing all reagents, tools, and software with identifiers (RRID or equivalent).
- The main text (Introduction, Results, Discussion) is narrative-focused; figure panels drive the mechanistic argument step by step.
- Figures are elaborate and multi-panel; the expectation is that each figure tests or validates a distinct mechanistic point; "one figure = one mechanistic claim" is the underlying logic.
- Graphical abstracts and eTOC blurbs are required or strongly expected (re-check current requirements); these communicate the advance visually and succinctly.
- Supplemental information carries secondary validations, extended datasets, and additional controls — but the main-text figures must establish the full mechanistic case without requiring the reader to consult the supplement for core evidence.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Cell author instructions" or "Cell Press information for authors" and follow the current version.
- Re-check article types, word and figure limits, and abstract format (structured vs. unstructured — re-check current requirements).
- Re-check STAR Methods requirements: Key Resources Table format, subheading structure, and method-detail expectations.
- Re-check graphical abstract and eTOC blurb requirements, format, and resolution specs.
- Re-check data/code/materials deposition requirements (GEO, SRA, PDB, Zenodo, GitHub) and accession-number submission timeline.
- Re-check ethics/consent for human or vertebrate-animal work; re-check reporting guidelines.
- Re-check competing-interests, funding, and AI-use disclosure policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence articulating the conceptual leap: what does the field now understand about cell or molecular biology that it did not before this paper?
- [ ] STAR Methods is complete, including the Key Resources Table with all reagents, antibodies, software, and datasets identified.
- [ ] Every major mechanistic claim has multiple orthogonal validations; no claim rests on a single assay.
- [ ] Data are deposited (or deposition confirmed) and accession numbers are in the manuscript; code is publicly available.
- [ ] Graphical abstract is drafted and meets current Cell Press format requirements.
- [ ] The discussion situates the mechanistic advance against the current leading models in the field — not just against older literature.

## Common desk-reject triggers

- A descriptive -omics study without mechanistic validation: cataloguing gene-expression changes or binding events without testing what they mean mechanistically.
- STAR Methods is absent, incomplete, or formatted incorrectly — Cell editors check this at intake.
- The advance is incremental within a known pathway without reframing or resolving a significant mechanistic controversy.
- The central mechanism is validated only biochemically in cells, when the field expectation includes in vivo models for the specific biology being claimed.
- The paper would fit `molecular-cell` (more structural/biochemical depth, tighter scope) or `nature-cell-biology` (cell biology, less molecular) but is submitted to Cell without justification for the broader significance.
- Missing graphical abstract or eTOC blurb at submission.

## Re-routing decision

- Exceptional significance for a cross-disciplinary science audience → `nature` or `science`.
- Mechanistic molecular biology at single-molecule/structural resolution, tighter scope than Cell → `molecular-cell`.
- Cell-biological mechanism without the molecular depth Cell requires → `nature-cell-biology` or `developmental-cell`.
- Stem-cell biology with mechanism and in vivo relevance → `cell-stem-cell`.
- Solid mechanistic advance below Cell's conceptual-leap bar → `current-biology`, `the-embo-journal`, or a Nature portfolio specialty journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cell
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there a complete mechanistic story with deep validation and STAR Methods-ready documentation?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <STAR Methods / Key Resources Table / graphical abstract / data deposition / ethics / article type>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
