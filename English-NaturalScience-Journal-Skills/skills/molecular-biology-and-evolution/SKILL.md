---
name: molecular-biology-and-evolution
description: Use when targeting Molecular Biology and Evolution (MBE) or deciding whether a molecular evolution manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Molecular Biology and Evolution (molecular-biology-and-evolution)

## Journal positioning

Molecular Biology and Evolution is the flagship research journal of the Society for Molecular Biology and Evolution (SMBE), published by Oxford University Press. It covers the quantitative study of molecular evolution, population genetics, phylogenetics, and the molecular basis of evolutionary change — emphasizing methodological rigor, inference under explicit evolutionary models, and the integration of genomic data with evolutionary theory. The readership is molecular evolutionists, population geneticists, phylogeneticists, and computational biologists who use sequence data and evolutionary models as primary tools. A paper must deliver either a new method with demonstrated performance advantages or a biological insight derived from rigorous molecular-evolutionary analysis — preferably both. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the MBE Oxford Academic site.

## When to trigger

- The author names MBE as the target venue for a molecular evolution, phylogenetics, or population-genetics study.
- A genomic or sequence-analysis study needs a rigorous molecular-evolutionary framing rather than a purely descriptive genomics or ecology framing.
- The author is developing a new statistical or computational method for phylogenetic inference, selection detection, or population-genetic analysis.
- The author is choosing between MBE, Genome Biology, and Nature Ecology & Evolution for a study integrating molecular evolution with ecology or genomics.

## Scope & topic fit

- Methods for phylogenetic inference, divergence-time estimation, ancestral-state reconstruction, and tree-based tests of evolutionary hypotheses.
- Population-genetic theory and inference: demographic modeling, coalescent-based methods, linkage-disequilibrium analysis, selection detection in natural populations.
- Molecular adaptation and positive selection: genome-wide scans for adaptive evolution, dN/dS modeling, codon evolution, signatures of polygenic adaptation.
- Evolutionary genomics: gene-family evolution, horizontal gene transfer, comparative genomics of molecular function, genome-size and structure evolution.
- Molecular clock and calibration: methodological advances in rate estimation, fossil calibration, relaxed-clock models.
- Molecular basis of phenotypic evolution: genotype-phenotype mapping, molecular convergence, evolutionary constraint and function.

## Method & evidence bar

- Methodological papers must demonstrate performance advantages over existing approaches via simulation studies, benchmarking on empirical data, and sensitivity analysis across model violations; software must be publicly available with documentation.
- Empirical molecular-evolution papers must use current best-practice statistical methods with explicit model justification; substitution models, selection tests, and demographic inferences must include uncertainty quantification.
- Population-genetic studies require appropriate sample sizes for the inferences made, phased or appropriately handled unphased data, and careful treatment of ascertainment bias and confounders.
- Claims of positive selection must address multiple-testing, population structure confounds, and demographic history; a single omega > 1 or FST outlier is insufficient.
- Data and code deposition (Dryad, Zenodo, GitHub) and sequence data deposition (GenBank, SRA) are expected for all empirical and methods papers.

## Structure & house style

- Research Articles are the primary format; Letters (shorter) exist for unusually rapid or compact advances — re-check current article-type options.
- The title should name the evolutionary question or methodological advance, not just the taxon or genome studied.
- Abstracts should state the evolutionary question, the analytical approach, the key result, and its significance to molecular evolutionary biology.
- Methods sections must be detailed enough to reproduce the analysis; references to code repositories and parameter files are expected.
- Simulation studies in methods papers should be presented in the main text if they are the primary validation, not relegated to supplementary materials.
- Figures for phylogenetic and population-genetic analyses should include uncertainty (bootstrap, posterior credibility intervals, confidence intervals on parameter estimates).

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Molecular Biology and Evolution author guidelines" and follow the current SMBE/OUP version.
- Re-check article-type and length limits; confirm the current definition and scope of Letters vs. Articles.
- Re-check data-deposition requirements: sequence data in GenBank/SRA, trees in Dryad/Zenodo/TreeBASE, code in a persistent repository with version tag.
- Re-check SMBE membership requirements (if any apply to submission fees), open-access options, and licence choices.
- Confirm competing-interests and funding disclosure, AI-use policy, and preprint compatibility (bioRxiv posting is generally supported).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the evolutionary question answered or the methodological advance delivered, and why it matters to molecular evolutionary biology.
- [ ] The analytical approach uses current best-practice methods with explicit model justification and uncertainty quantification.
- [ ] Claims of selection, divergence timing, or demographic history are robust to model-choice sensitivity and confounders.
- [ ] All sequence data, trees, scripts, and analysis pipelines are deposited in or linked to publicly accessible repositories.
- [ ] The paper is framed in the language of molecular evolution, not just genomics or ecology, to match MBE's readership.
- [ ] Simulation or benchmarking studies are complete and presented in sufficient detail.

## Common desk-reject triggers

- A descriptive comparative genomics paper that does not test an evolutionary hypothesis or advance molecular-evolutionary methodology.
- A phylogenetic study that merely extends an existing tree by adding taxa without addressing a phylogenetic question of broad significance.
- Population-genetic conclusions drawn from methods with known limitations (e.g., unaccounted structure in selection scans) without sensitivity analysis.
- Software papers without rigorous benchmarking, publicly available code, or documentation sufficient for independent use.
- An ecology study that uses sequence data incidentally but does not engage with molecular-evolutionary theory or inference.

## Re-routing decision

- Conceptual advance in ecology or macroevolution using molecular data: `nature-ecology-and-evolution` (broader biological significance and cross-scale framing).
- Genomics-methods paper with scope beyond molecular evolution: `genome-biology` (broader computational biology audience).
- Population genetics with medical/human genomics framing: Nature Genetics (`nature-genetics`) or American Journal of Human Genetics.
- Broad evolutionary biology with fossil and living record integration: `nature-ecology-and-evolution` or Current Biology (`current-biology`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Molecular Biology and Evolution
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the molecular-evolutionary rigor — explicit models, benchmarking, uncertainty — clear the MBE bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / data-code deposition / open-access options / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
