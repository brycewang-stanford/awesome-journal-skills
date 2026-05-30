---
name: cc-study-design
description: Use when designing or auditing the experimental plan for a Cancer Cell (Cell Press) study — orthogonal validation across in vitro, in vivo, and human tumor systems, with controls, replicates, power, randomization, and blinding. It plans design; it does not run statistics or write figures.
---

# Experimental Design (cc-study-design)

## When to trigger

- The mechanism rests on a single system (e.g., cell lines only)
- Reviewers will ask "is this true in vivo?" or "does it hold in patients?"
- Controls, replicates, or sample-size logic are unclear
- Planning mouse / PDX / organoid experiments and unsure about rigor elements

## Orthogonal validation ladder

Cancer Cell expects a mechanism corroborated across **independent, complementary systems**. Build the strongest ladder the biology allows:

| Layer | Systems | Role |
|-------|---------|------|
| In vitro | Cell lines (multiple, authenticated), primary cells, co-cultures, biochemistry | Establish mechanism, gain/loss-of-function, epistasis |
| Functional genetics | CRISPR KO/KI, shRNA/siRNA with rescue, point mutants, degrons | Causality and specificity |
| In vivo | GEMM, syngeneic, xenograft, **PDX**, orthotopic, metastasis models | Mechanism operates in a tumor in an organism |
| 3D / ex vivo | Tumor **organoids**, patient-derived organoids, slice cultures, spheroids | Bridge to human, drug response |
| Human | Patient tumor samples, TMAs, scRNA-seq, public cohorts (TCGA), outcome data | Translational anchor / clinical relevance |

A Cancer Cell paper typically spans in vitro + in vivo + a human anchor. Decide early which layers carry the **causal** claim and which provide corroboration.

## Controls (the parts reviewers attack)

- **Genetic perturbation:** include rescue / add-back; use ≥2 independent sgRNAs or shRNAs (or rule out off-target); non-targeting / scramble control matched to delivery.
- **Pharmacology:** vehicle control, dose-response, on-target genetic phenocopy, and where possible a resistant mutant or analog.
- **In vivo:** isotype/vehicle controls, littermate or co-housed controls for GEMMs, tumor-volume and endpoint pre-defined.
- **Antibody / staining:** isotype, KO/KD-validated, single-stain compensation for flow.

## Replicates: biological vs technical

- **Biological replicates** = independent biological units (separate mice, independent cell passages/cultures, distinct patients). These define `n`.
- **Technical replicates** (duplicate wells, repeat measurements) reduce measurement noise but **do not** increase `n`.
- Report both clearly; never inflate `n` with technical replicates (see `cc-statistics`).

## Sample size, randomization, blinding (especially animals)

- **Power / sample size:** justify mouse `n` (effect size + variance from pilot or literature); state the basis even if informal.
- **Randomization:** allocate animals to arms randomly (e.g., when tumors reach a set volume), not by cage convenience.
- **Blinding:** blind outcome assessment (tumor measurement, histology scoring, imaging quantification) wherever feasible.
- **Inclusion/exclusion:** pre-define humane endpoints and exclusion criteria; report all animals/samples and any exclusions.

## Human-sample design

- Define cohort, inclusion/exclusion, and how samples link to outcomes.
- Power survival / association analyses; pre-specify primary comparison.
- Note IRB/consent (route to `cc-ethics-registration`).

## Checklist

- [ ] Mechanism validated across ≥2 orthogonal systems; causal layer identified
- [ ] In vivo evidence present (GEMM / xenograft / PDX / orthotopic) where claims require it
- [ ] Genetic perturbations include rescue and ≥2 independent reagents
- [ ] Matched controls defined for every perturbation and treatment
- [ ] Biological vs technical replicates distinguished; `n` = biological units
- [ ] Animal sample size justified; randomization and blinding specified
- [ ] Inclusion/exclusion criteria and humane endpoints pre-defined
- [ ] Human-sample cohort and primary comparison pre-specified

## Anti-patterns

- Conclusions from a single cell line or a single system
- shRNA/CRISPR phenotype with no rescue (off-target not excluded)
- "n=3" that is three wells of one experiment (pseudo-replication)
- Mouse experiments with no randomization, no blinding, no power basis
- Therapeutic efficacy claimed without an in vivo tumor model
- Selecting samples post hoc to fit the hypothesis

## Output format

```
【Causal claim layer】in vitro / in vivo / human
【Orthogonal systems planned】...
【Controls per perturbation】rescue + 2 reagents? vehicle/isotype?
【Replicates】biological n = ... ; technical handled separately
【Animal rigor】power basis / randomization / blinding / endpoints
【Human anchor】cohort + primary comparison
【Gaps to close before submission】...
【Next step】cc-reporting-standards (rigor reporting) or cc-statistics
```
