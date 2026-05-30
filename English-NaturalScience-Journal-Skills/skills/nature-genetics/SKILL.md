---
name: nature-genetics
description: Use when targeting Nature Genetics or deciding whether a genetics/genomics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Genetics (nature-genetics)

## Journal positioning

Nature Genetics is the Nature Portfolio's flagship genetics and genomics journal, publishing studies that advance understanding of the genetic basis of biological processes or disease — either through population-scale genomic discovery (GWAS, whole-genome sequencing, multi-ancestry analyses) or through functional genomics that mechanistically interprets genetic variation. The defining editorial expectation is that a discovery at the genomic or genetic level must be either exceptionally large in scale and rigorously interpreted, or paired with functional mechanistic follow-through that converts a statistical association into biological insight. The readership spans geneticists, genomicists, computational biologists, and disease biologists.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site or submission system.

## When to trigger

- The author names Nature Genetics as the target venue.
- A GWAS, multi-ancestry genomics, or large-scale sequencing study is assessing whether its scale and biological interpretation meet the bar.
- A functional genomics study (CRISPR screens, eQTL mapping, chromatin architecture, regulatory element dissection) needs to assess its significance level.
- The author is choosing between Nature Genetics, Nature Human Genetics, American Journal of Human Genetics, or a disease-specific journal.

## Scope & topic fit

- Population genetics and complex trait genomics: large-scale GWAS, multi-ancestry meta-analyses, polygenic architecture, heritability partitioning — when the biological interpretation is substantive, not merely incremental.
- Functional genomics and gene regulation: eQTL, sQTL, chromatin accessibility, 3D genome organization, regulatory element function — interpreted mechanistically or in disease context.
- Rare-variant discovery in cohorts or families: Mendelian disease gene identification or de novo variant studies when the biology is novel and the phenotyping is rigorous.
- Somatic genetics and cancer genomics: mutational signatures, driver gene discovery, clonal dynamics — at population or multi-tumor scale.
- Single-cell genomics applied to genetic or epigenomic questions: cell-type-specific eQTLs, single-cell ATAC-seq in genetic context — when the genetic question drives the analysis.
- Evolutionary and population genetics: demographic inference, selection scans, admixture — when the finding reframes human or organismal genetic history significantly.

## Method & evidence bar

- Scale is a distinguishing feature: GWAS and multi-ancestry studies must be sufficiently powered and must go beyond listing loci to interpreting functional and biological mechanisms.
- Functional follow-through is increasingly expected: statistical genomic discoveries should be accompanied by experimental validation (reporter assays, allele-specific expression, CRISPR perturbation, animal model) or by strong computational evidence linking variants to regulatory mechanism.
- Computational methods and statistical rigor: appropriate multiple-testing correction (genome-wide significance thresholds), LD score regression, conditional analyses, and fine-mapping; inflated signals must be addressed.
- Diversity and ancestry: multi-ancestry analyses are the current standard; single-ancestry studies should justify scope and acknowledge limitations.
- Data sharing: GWAS summary statistics, individual-level data access agreements, and code deposition are expected; Nature Portfolio reporting summary required.
- Reproducibility: replication cohorts or independent functional validation strengthens genomic discovery claims.

## Structure & house style

- Nature Portfolio format: unstructured abstract (re-check the current length limit); main text with no mandatory STAR Methods equivalent, but Methods section must be complete and well-organized.
- Extended Data figures (up to 10 typically; re-check current limit) carry additional analyses; Supplementary Information carries large tables, code, and extended methods.
- Nature reporting summary required (all Nature Portfolio research journals); covers study design, statistics, data sharing, and field-specific reporting.
- Titles should be informative and accessible to a broad genetics audience; avoid highly technical jargon.
- The introduction establishes the genetic question and its significance; the contribution is stated explicitly and distinguished from previous GWAS or functional genomics studies.
- Data/code availability statement required; summary statistics should be deposited to GWAS Catalog or equivalent.

## Official-submission checklist

- Search "Nature Genetics author information" on the Nature Portfolio site and follow the current version.
- Re-check article types (Article vs. Brief Communication vs. Letter — format names may have changed; re-check), length and figure limits, and Extended Data policy.
- Confirm Nature reporting summary requirements and any genetics-specific checklists (e.g., ARRIVE for animal studies, human-subjects consent).
- Re-check data availability requirements: GWAS Catalog deposition, SRA/dbGaP for raw sequencing, code on GitHub/Zenodo.
- Verify competing-interests, funding, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/APC options.
- Re-check the current multi-ancestry and diversity reporting expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the genetic or genomic principle established and its significance beyond the immediate trait or disease.
- [ ] The advance goes beyond locus discovery: functional or mechanistic interpretation is substantive.
- [ ] Multi-ancestry representation and population diversity are addressed in the study design and limitations.
- [ ] Multiple-testing, LD, and confounding are handled appropriately; genome-wide significance thresholds are applied.
- [ ] GWAS summary statistics or equivalent data are ready for deposition; code is documented and deposited.
- [ ] Nature reporting summary is prepared; data/code availability statement is complete.

## Common desk-reject triggers

- A single-ancestry GWAS that identifies loci already known or trivially close to known signals, with no functional interpretation.
- Functional genomics study (chromatin, eQTL) without a clear genetic question or disease connection and insufficient scale for Nature Genetics significance.
- Computational genomics tool paper where the primary advance is the method, not the biological discovery — better suited to `nature-methods` or `genome-biology`.
- Clinical genetics study (variant classification, population prevalence of a Mendelian condition) below the discovery significance threshold — better suited to American Journal of Human Genetics or Genetics in Medicine.
- Analyses with inflated genomic signals (lambda inflation unaddressed), inadequate multiple-testing correction, or missing replication in independent cohorts.

## Re-routing decision

- Strong genetic discovery in a specific disease area with clinical implications → `nature-medicine` (if translational impact is primary) or a disease-specific journal.
- Excellent functional genomics or gene-regulation study → `nature-cell-biology` (if cell biology is primary) or `molecular-cell` (if molecular mechanism dominates).
- Large-scale genomics below Nature Genetics significance → `nature-communications`, `genome-biology`, or `plos-genetics`.
- Methods-first genomics tool with biological application → `nature-methods` or `genome-biology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Genetics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the scale + functional interpretation clear Nature Genetics's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Extended Data limit / reporting summary / GWAS Catalog deposition / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
