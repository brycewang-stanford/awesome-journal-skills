---
name: immunity
description: Use when targeting Immunity or deciding whether an immunology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Immunity (immunity)

## Journal positioning

Immunity is Cell Press's flagship immunology journal, publishing mechanistic studies that define how immune cells develop, are activated, regulated, and mediate host defense or inflammatory disease — grounded in in vivo biology. The readership is the global immunology community: basic immunologists, immunopathologists, and translational researchers studying autoimmunity, infection, cancer immunology, and immune-mediated disease. Papers must reveal a mechanistic principle that reshapes how the field understands an immune process; descriptive immunophenotyping or cataloguing without mechanism does not reach the bar.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Immunity as the target venue.
- A mechanistic immunology study is choosing between Immunity, Nature Immunology, Science Immunology, or Journal of Experimental Medicine.
- A manuscript in cancer immunology or infection immunology needs to assess whether the immunological mechanism — rather than the cancer or pathogen biology — is the primary advance.
- The author needs Immunity's specific desk-reject triggers and a ranked alternative list.

## Scope & topic fit

- T cell biology: differentiation, exhaustion, memory, effector programs, regulatory circuits — mechanistically driven by in vivo models or human translational data.
- Innate immunity: pattern recognition, inflammasome biology, innate cell lineage specification and activation, trained innate immunity mechanisms.
- B cell biology, antibody responses, germinal center reactions, and humoral memory — at the mechanistic level.
- Cytokine and co-stimulatory signaling: receptor proximal signaling cascades, transcriptional regulators, epigenetic control of immune-cell identity.
- Cancer immunology when the immune-cell mechanism is the central advance, not the tumor biology.
- Autoimmunity and inflammatory disease mechanisms: tolerance breakdown, tissue-resident immune cell function, regulatory T cell failure modes.

## Method & evidence bar

- In vivo validation is essentially mandatory: genetic mouse models (conditional knockouts, fate mapping, bone-marrow chimeras), adoptive transfer, or infection models are the standard.
- Mechanistic depth expected: identify the pathway, the transcription factor, the epigenetic modification, or the receptor-ligand pair, and validate with epistasis or rescue.
- Single-cell genomics (scRNA-seq, ATAC-seq) and multi-omic data are expected to be hypothesis-generating inputs, not standalone deliverables; functional validation in vivo is required.
- Human translational data — patient cohorts, ex vivo stimulation, or clinical specimens — substantially strengthens papers and is expected for disease-relevant studies.
- STAR Methods required; data deposited to GEO, Sequence Read Archive, or equivalent; flow-cytometry data deposited per community standards (MIFlowCyt).
- Statistical rigor: replicates (biological not technical) specified, appropriate multiple-comparison correction, and experimental group sizes justified.

## Structure & house style

- STAR Methods mandatory; key resources table covering antibodies, mouse strains, cell lines, oligonucleotides, and software.
- Declarative, mechanism-first title; structured abstract with "in brief" / highlights summarizing the immunological advance.
- Figures build from genetic and cellular phenotype through mechanistic dissection to in vivo disease relevance; the narrative arc should be complete within the main figures.
- Graphical abstract required (Cell Press standard); source data for all quantitative plots.
- The introduction situates the study within the mechanistic immunology literature — not epidemiology of disease burden — and closes with a clear statement of the advance.
- Data/code availability statement; any custom analysis code should be deposited in a public repository.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Immunity author information" on the Cell Press site and follow the current version.
- Re-check article types (Article vs. Short Article), length and figure limits, and supplemental policy.
- Confirm STAR Methods and key resources table requirements.
- Re-check animal ethics (IACUC/equivalent) and human-subjects approvals, consent, and institutional review documentation.
- Verify flow-cytometry data deposition requirements and sequencing data deposition.
- Re-check competing-interests, funding, author-contributions, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating which mechanistic immunological principle is established by this paper.
- [ ] The advance is a mechanistic insight into an immune process, not a phenotype catalogue or disease association.
- [ ] In vivo evidence is central; the genetic perturbation is validated with at least one orthogonal approach.
- [ ] Human translational data or patient-cohort validation is included or its absence is justified.
- [ ] STAR Methods, key resources table, flow-cytometry and sequencing data deposition are prepared.
- [ ] The framing positions the advance against the current mechanistic canon in this immune process.

## Common desk-reject triggers

- Immunophenotyping study — detailed flow-cytometry characterization of an immune compartment — without a mechanistic molecular explanation.
- Single-cell atlas or transcriptomics data without functional validation; the data is interesting but the biology is not resolved.
- In vivo work entirely in cell culture with immunological readouts but no model organism validation for the mechanistic claim.
- Cancer immunology paper where the tumor biology, not the immune mechanism, is the primary advance — better suited to `cancer-cell`.
- Descriptive correlation between an immune parameter and a clinical outcome without mechanistic insight.

## Re-routing decision

- Equivalent mechanistic depth with stronger translational/clinical story → `nature-immunology` (often favors highest-profile mechanism + translational impact) or `science-immunology` (AAAS, broad-significance immunology).
- Classical mechanistic immunology at slightly lower overall significance → `journal-of-experimental-medicine` (Rockefeller; rigorous in vivo immunology).
- Mechanistic immunology in infectious context → `cell-host-and-microbe` if the host-pathogen interaction is the primary frame.
- Solid mechanistic work below Immunity significance → `elife`, `plos-biology`, or Journal of Immunology / European Journal of Immunology.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Immunity
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the in vivo mechanism + validation clear Immunity's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / STAR Methods / flow-cytometry data / animal & human ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
