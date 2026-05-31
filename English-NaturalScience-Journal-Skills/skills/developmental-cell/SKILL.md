---
name: developmental-cell
description: Use when targeting Developmental Cell or deciding whether a developmental or cell-biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Developmental Cell (developmental-cell)

## Journal positioning

Developmental Cell is Cell Press's dedicated venue for developmental biology and cell biology, publishing mechanistic studies of how cells are built, how they acquire identity, divide, migrate, and organize into tissues and organs — and how these processes go wrong in disease. The journal uniquely bridges classical developmental genetics (fate specification, morphogenesis, organogenesis) and modern cell biology (cytoskeletal dynamics, organelle biology, cell polarity, the cell cycle) under a single mechanistic umbrella. The readership spans developmental biologists, cell biologists, and stem-cell researchers; studies need a clear mechanistic principle, not just an in vivo phenotype.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Developmental Cell as the target venue.
- A study straddles developmental biology and cell biology and the author is choosing between Developmental Cell, Current Biology, and Nature Cell Biology.
- A mechanistic morphogenesis or organogenesis study needs to assess whether its cell-biological resolution meets the bar.
- The author needs Developmental Cell's desk-reject risks and credible alternatives.

## Scope & topic fit

- Cell-fate specification and transcriptional control of identity: master regulators, lineage commitment, and reprogramming — studied mechanistically in a developmental context.
- Morphogenesis and tissue organization: cell migration, collective cell dynamics, polarity, tissue mechanics, and morphogen gradients — with molecular mechanism.
- Organogenesis and organ patterning: how specific organs assemble during development, studied in model organisms or organoids with mechanistic depth.
- Cell-biological processes with developmental context: mitosis, cytokinesis, organelle dynamics, protein quality control, cell death — when the developmental role is demonstrated.
- Stem-cell biology and regeneration: adult stem-cell niche, regeneration mechanisms, transdifferentiation — mechanism is primary.
- Cell signaling in development: Wnt, Notch, Hedgehog, FGF, BMP pathway mechanics in a developmental or cell-biological setting.

## Method & evidence bar

- Genetic and molecular mechanism is required: identification of the gene/pathway is not the advance; understanding how and why it acts in the developmental or cell-biological context is.
- Model-organism work (C. elegans, Drosophila, zebrafish, Xenopus, mouse) or organoids with rigorous genetic perturbations (knockout, dominant-negative, rescue) expected.
- Cell biology studies should integrate live imaging, quantitative morphometry, or biochemical dissection; the field values high-quality time-lapse and confocal data with quantitation.
- Epistasis or rescue experiments linking the molecular mechanism to the developmental phenotype; a loss-of-function phenotype alone is not the bar.
- STAR Methods required; reagents (cell lines, strains, plasmids) deposited to Addgene or equivalent; imaging data quantified.
- Proteomics, transcriptomics, or genomics data should be mechanistically interpreted; surveys alone are not advances at this venue.

## Structure & house style

- STAR Methods mandatory; key resources table covering antibodies, organisms/strains, recombinant proteins/plasmids, and software.
- Declarative, mechanism-forward title; avoid question titles or purely descriptive phenotype titles.
- Cell Press structured abstract with "in brief" / highlights summarizing the developmental/cell-biological mechanism.
- Main figures should narrate the mechanistic story: identify the phenotype, locate the cellular/tissue site of action, define the molecular mechanism, rescue or epistasis confirmation.
- High-quality fluorescence micrographs are central to this venue; image panels must be publication-quality and quantified.
- Source data for all quantitative plots; data/code availability statement required.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Developmental Cell author information" on the Cell Press site and follow the current version.
- Re-check article types (Article, Short Article, Resource), length and figure limits, and supplemental policy.
- Confirm STAR Methods and key resources table requirements.
- Re-check animal ethics and human-subjects documentation where applicable.
- Verify strain/plasmid deposition and imaging data requirements.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the developmental or cell-biological mechanism discovered.
- [ ] The advance goes beyond phenotype: the molecular mechanism is defined, not just implied.
- [ ] Epistasis or rescue experiments validate the mechanistic model.
- [ ] Image data are quantified; key morphological claims are supported by rigorous morphometry or live imaging.
- [ ] STAR Methods, key resources table, and reagent/data deposition are prepared.
- [ ] The framing positions the advance against the mechanistic canon in this developmental process or cell-biological question.

## Common desk-reject triggers

- Purely phenotypic study in a model organism: a gene is required for a process, but how it acts mechanistically is not addressed.
- Cell-biology study with no developmental context and no cell-biological mechanism — better suited to a cell-biology-focused journal.
- Transcriptomics or genomics atlas of a developmental process without mechanistic follow-through in vivo.
- Organoid paper that describes a differentiation protocol or a morphological phenotype without defining the underlying molecular principle.
- Studies where the primary advance is a disease-biology or clinical insight rather than a developmental or cell-biological mechanism — better suited to `cancer-cell`, `cell-stem-cell`, or disease-focused venues.

## Re-routing decision

- Very strong cell-biology mechanism with less developmental context → `nature-cell-biology` (deeper cell-biology emphasis) or `molecular-cell` (if the mechanism is molecular/structural).
- Equally strong developmental advance with broad organismal or evolutionary significance → `current-biology` (Cell Press; broader biology scope) or `nature` / `science` if significance is exceptional.
- Stem-cell biology as the primary advance with regeneration or therapeutic angle → `cell-stem-cell`.
- Solid mechanistic study below Developmental Cell significance → `elife`, `development`, or `plos-biology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Developmental Cell
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the developmental/cell-biology mechanism + genetic validation clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / STAR Methods / imaging data / animal ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
