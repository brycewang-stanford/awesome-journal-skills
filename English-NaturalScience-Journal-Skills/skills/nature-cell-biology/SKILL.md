---
name: nature-cell-biology
description: Use when targeting Nature Cell Biology or deciding whether a cell-biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Cell Biology (nature-cell-biology)

## Journal positioning

Nature Cell Biology is the Nature Portfolio's flagship cell-biology journal, publishing mechanistic studies that deliver conceptual advances in how cells are organized, how they communicate and signal, how they maintain or break homeostasis, and how cell-biological processes underlie physiology and disease. The journal has a distinctively cell-biological identity — cytoskeletal dynamics, organelle biology, membrane trafficking, cell polarity, cell death, cell cycle, and intercellular signaling — that distinguishes it from Nature Genetics (genetics-centered) and the Cell Press developmental journals. Papers are expected to reveal a general cell-biological principle, not merely characterize a phenotype in one cell type. The readership is cell biologists broadly and adjacent biological disciplines.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site or submission system.

## When to trigger

- The author names Nature Cell Biology as the target venue.
- A cell-biology study is choosing between Nature Cell Biology, Developmental Cell, Molecular Cell, and the Journal of Cell Biology.
- A mechanistic study of a cell-biological process in a disease or developmental context needs to assess its significance level and framing for this venue.
- The author needs Nature Cell Biology's desk-reject triggers and credible re-routing options.

## Scope & topic fit

- Cytoskeletal regulation and cell mechanics: actin, microtubule, and intermediate-filament dynamics; motor proteins; cell migration and mechanical force generation — mechanistically defined.
- Organelle biology and membrane trafficking: ER, Golgi, lysosome, mitochondria, peroxisome, and autophagy — biogenesis, dynamics, and inter-organellar communication at the molecular level.
- Cell signaling and receptor biology: how extracellular signals are sensed, transduced, and integrated at the cell-biological level — not merely a pathway description.
- Cell cycle, cell division, and genome stability: mitosis, cytokinesis, checkpoint mechanisms, DNA damage response — cell-biological mechanism.
- Cell death mechanisms: apoptosis, necroptosis, pyroptosis, ferroptosis — molecular mechanism and cell-biological execution.
- Intercellular communication: exosomes, tunneling nanotubes, cell-cell junctions, paracrine signaling — when the cell-biological mechanism of communication is the advance.
- Cell-biological basis of cancer, neurodegeneration, or metabolic disease — when the cell-biological process, not the disease phenotype, is the primary advance.

## Method & evidence bar

- Conceptual advance at the cell-biological level is the central criterion: the paper should change how the field thinks about a cell-biological process.
- High-quality imaging is a hallmark of this venue: live-cell imaging, super-resolution, cryo-ET, or quantitative fluorescence microscopy expected for cell-biological claims; image data must be quantified.
- Genetic dissection: knockout/knockin, RNAi/CRISPR, dominant-negative constructs, rescue experiments — orthogonal validation of the key mechanistic claim.
- Biochemical validation: co-immunoprecipitation, proximity labeling, structural data, or reconstitution assays supporting the molecular mechanism.
- In vivo relevance: animal model or human cell validation supports but does not always gate acceptance; a compelling cell-biological principle in cultured cells can suffice if the mechanism is general.
- Nature reporting summary required; source data for all quantitative figures; code/analysis scripts deposited.

## Structure & house style

- Nature Portfolio format: unstructured abstract; main text with Methods section; Extended Data figures for additional mechanistic validation and controls; Supplementary Information for large data.
- Nature reporting summary required; any animal or human-subjects work must include appropriate ethics documentation.
- Titles should state the cell-biological mechanism or principle; they should be accessible to cell biologists not specialized in the specific organelle or process.
- The introduction defines the cell-biological question and its significance for understanding cell function or disease — not a recitation of molecular players already known.
- Results should progress: observe the cell-biological phenomenon, identify the molecular components, dissect mechanism, establish generality or in vivo relevance.
- Imaging data must include quantification (track statistics, fluorescence intensity profiles, colocalization coefficients); representative images alone are insufficient.

## Official-submission checklist

- Search "Nature Cell Biology author information" on the Nature Portfolio site and follow the current version.
- Re-check article types (Article vs. Brief Communication), length and figure limits, and Extended Data policy.
- Confirm Nature reporting summary requirements and any microscopy-specific reporting standards (e.g., image acquisition parameters, quantification methods).
- Re-check animal ethics, human-subjects, and biosafety documentation where applicable.
- Verify data/code/imaging data deposition requirements (EMDB for cryo-EM, image repositories as applicable).
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the cell-biological principle established and why it is general — not tied to only one cell type or context.
- [ ] The mechanistic claim is supported by at least two orthogonal approaches (imaging + biochemistry, or genetics + imaging).
- [ ] Quantitative image analysis (not just representative panels) supports all major imaging-based claims.
- [ ] In vivo relevance or cross-cell-type generality is established or the argument for generality is explicit.
- [ ] Nature reporting summary, Extended Data, and data/code deposition are prepared.
- [ ] The framing positions the advance against the current cell-biological understanding, not against disease incidence.

## Common desk-reject triggers

- A mechanistic study in which the cell biology is the context but the real advance is molecular (better for `molecular-cell`) or developmental (better for `developmental-cell`).
- Purely phenotypic study: a protein is required for a cell-biological process, but the mechanism by which it acts is not addressed.
- Imaging paper with no quantification and no mechanistic follow-through; beautiful microscopy alone does not constitute a conceptual advance.
- Cell-biological study confined to one highly specialized cell type or organism with no argument for the generality of the mechanism.
- A disease or cancer study where the cell-biological mechanism is supporting context, not the primary advance — better suited to `cancer-cell`, `developmental-cell`, or `nature-genetics`.

## Re-routing decision

- Equal depth but mechanism is molecular/structural rather than cell-biological → `molecular-cell` (ACS; molecular-to-structural level) or `nature-structural-and-molecular-biology`.
- Strong cell biology in a developmental context → `developmental-cell` (Cell Press; developmental biology breadth).
- Genetics or gene-regulation advance using cell-biology tools → `nature-genetics` or `molecular-cell`.
- Excellent cell-biology below Nature Cell Biology significance → `elife`, Journal of Cell Biology, or `current-biology` (`current-biology` for particularly novel or cross-disciplinary cell biology).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Cell Biology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the cell-biological mechanism + imaging rigor + generality clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Extended Data / reporting summary / imaging quantification / data-code deposition>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
