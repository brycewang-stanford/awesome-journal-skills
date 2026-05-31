---
name: nature-methods
description: Use when targeting Nature Methods or deciding whether a methods/tools manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Methods (nature-methods)

## Journal positioning

Nature Methods is the Nature Portfolio's dedicated venue for new methods, approaches, and technologies in the life sciences and related disciplines, with the distinguishing requirement that a published method must be generalizable — applicable by other researchers to their own biological questions — and thoroughly benchmarked against alternatives. The journal's editorial culture is highly skeptical of incremental improvements; what wins is a genuinely new capability or a step-change in performance that enables previously impossible or impractical experiments. The readership is broadly all life scientists who need to understand and adopt new tools, making technical clarity and honest benchmarking as important as scientific novelty.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site or submission system.

## When to trigger

- The author names Nature Methods as the target venue.
- A new method, computational tool, or technology platform is being submitted and the author is choosing between Nature Methods, Nature Biotechnology, Genome Biology, or Bioinformatics.
- A biological study whose primary advance is a new analytical or experimental tool needs to assess whether the method's generalizability and benchmarking meet the bar.
- The author needs Nature Methods' specific desk-reject triggers and re-routing options.

## Scope & topic fit

- New experimental techniques in imaging, sequencing, proteomics, metabolomics, structural biology, or single-cell analysis — when the method enables previously impossible or substantially more efficient experiments.
- Computational and statistical methods for biology: new algorithms for sequence analysis, spatial transcriptomics, protein structure prediction, variant calling, or multi-omics integration — when rigorously benchmarked.
- Synthetic-biology and genome-engineering tools: new CRISPR variants, base editors, prime editors, or delivery systems — when generalizability and performance are demonstrated at method level.
- Microscopy and biophysical methods: super-resolution, live-cell imaging, cryo-EM workflows, single-molecule techniques — when the methodological advance is the contribution.
- Organoid, organ-on-chip, or model-system methods when the platform itself (not only its biological application) is the advance.
- Data analysis pipelines and benchmarking studies for widely used method classes — when the result changes best practices across the community.

## Method & evidence bar

- Generalizability is the primary test: the method must be demonstrated to work on multiple biological systems or datasets, not just the authors' system of development.
- Benchmarking against the current best alternatives is mandatory, using objective performance metrics; claims of superiority must be supported by head-to-head comparison on the same datasets or experimental conditions.
- Biological application is required: a method must demonstrate what new biology it enables or what question it answers; a pure engineering advance without biological demonstration does not qualify.
- Code or protocols for methods that generate data must be made fully available; software tools must be well-documented, installable, and actively maintainable.
- Usability matters: the editorial board values tools that other labs can actually adopt; inaccessible instruments or reagents requiring specialized infrastructure weaken the case.
- Reproducibility reporting: Nature reporting summary required; reagents and protocols should be described in sufficient detail for independent replication.

## Structure & house style

- Nature Portfolio format: unstructured abstract; main text followed by Methods section; Extended Data figures (up to current limit) for additional benchmarking; Supplementary Information for large datasets, code, and extended protocols.
- Nature reporting summary required; methods-specific checklists (e.g., ARRIVE for animal-based validation, human-subjects for clinical data) where applicable.
- The introduction must establish the biological problem the method solves and why existing approaches are insufficient; avoid leading with engineering specifications.
- Results should be organized as: (1) method concept and design, (2) performance validation, (3) benchmarking against alternatives, (4) biological demonstration.
- Figures should include performance metrics with error bars, representative data showing the biological application, and honest failure-mode analysis.
- Code deposited in a public repository (GitHub, Zenodo); a stable versioned release should accompany submission; protocols deposited to protocols.io where appropriate.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Nature Methods author information" on the Nature Portfolio site and follow the current version.
- Re-check article types (Article, Brief Communication, Analysis), length and figure limits, and Extended Data policy.
- Confirm Nature reporting summary requirements and any field-specific checklists.
- Re-check code/software deposition and documentation standards (README, installation, example data).
- Verify data availability: raw benchmarking data, test datasets, and protocol deposition requirements.
- Re-check competing-interests (particularly tool-commercialization disclosures), funding, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what new experimental or analytical capability this method provides that was previously impossible or substantially impractical.
- [ ] Benchmarking against the current best alternatives is complete, objective, and uses the same evaluation conditions.
- [ ] The method is demonstrated in at least two biological contexts or datasets to establish generalizability.
- [ ] Code or protocols are fully documented, deposited, and independently installable/reproducible.
- [ ] Nature reporting summary is prepared; biological application data show what new biology the method enables.
- [ ] Usability for a typical lab — reagent access, computational requirements — is honestly assessed.

## Common desk-reject triggers

- A method demonstrated only on the authors' own biological system with no generalizability evidence.
- Incremental improvement over an existing method — faster by 10%, slightly better sensitivity — without a step-change in capability or a qualitatively new application.
- A computational tool paper without rigorous benchmarking against current alternatives on publicly available datasets.
- A method paper where the biological discovery, not the method, is the real advance — better submitted to the appropriate biology journal.
- Code is not released, is available only on reasonable request, or is undocumented and non-reproducible.

## Re-routing decision

- New method primarily enabling biotech/therapeutic applications → `nature-biotechnology` (broader applied-science scope, more tolerant of translational framing).
- Genomics/bioinformatics tool with strong biological application → `genome-biology` (OA, bioinformatics-friendly, benchmark papers welcome).
- Excellent method below Nature Methods significance or generalizability bar → `nature-communications`, Bioinformatics, or a specialty methods journal.
- New method for a specific biological field where the biology is the primary advance → the relevant biology journal (e.g., `neuron` for a neuroscience imaging technique).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Methods
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the method generalizable, benchmarked, and enabling of new biology?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Extended Data limit / reporting summary / code deposition / protocols / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
