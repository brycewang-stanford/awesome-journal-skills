---
name: nejm-statistics
description: Use to enforce NEJM's clinical statistical reporting — confidence intervals over bare P values, the pre-specified intention-to-treat primary analysis, multiplicity control for secondary endpoints, pre-specified subgroups with interaction tests, missing-data handling, and absolute risk with NNT alongside relative measures.
---

# Clinical Statistics & Reporting (nejm-statistics)

## When to trigger

- Results report P values without confidence intervals.
- The primary analysis population (ITT vs per-protocol) is unclear.
- Many secondary endpoints are tested with no multiplicity plan.
- Subgroup findings are highlighted without pre-specification or interaction tests.
- Only relative risk is reported, with no absolute risk or NNT.

## Confidence intervals over bare P values

NEJM's statistical reporting guidance favors **effect estimates with 95% confidence intervals** over bare significance tests.

- [ ] Every primary and key secondary outcome: **effect estimate + 95% CI** (HR/RR/OR or mean difference).
- [ ] Report **exact P values** (e.g., P=0.03), not "P<0.05", except for very small values.
- [ ] A CI that includes the null is not "no difference" — report the estimate and its width; interpret precision.
- [ ] For observational data, use **cautious, non-causal language** (associated with, not causes).

## The pre-specified primary analysis

- The **primary outcome** is single and pre-specified; its analysis follows the SAP.
- **Intention-to-treat** is the primary analysis population for superiority trials; **per-protocol** is a sensitivity analysis. (For non-inferiority, both ITT and per-protocol matter — report both.)
- State the analysis model (e.g., Cox, logistic, mixed model) and pre-specified covariates/stratification.

## Multiplicity (the secondary-endpoint trap)

- Pre-specify a **testing hierarchy** or a multiplicity adjustment (e.g., gatekeeping, Hochberg, Bonferroni) for multiple primary/secondary endpoints.
- Endpoints **not** in the controlled testing scheme are **exploratory** — say so, and report estimates with CIs but no inferential P claims.
- Do not declare a secondary endpoint "significant" if it sits outside the multiplicity plan.

## Subgroups (warn against over-interpretation)

- Subgroup analyses must be **pre-specified**; label post-hoc subgroups as exploratory.
- Test the **interaction** (treatment × subgroup), not just within-subgroup P values — a within-subgroup "significant" effect without a significant interaction is weak evidence.
- Present subgroups in a **forest plot** with interaction P values (see `nejm-figures-tables`).
- Do not let a subgroup result become the headline of an otherwise null trial.

## Absolute risk and NNT

- Report **absolute risk difference** alongside relative measures — a large relative reduction on a rare outcome can be a tiny absolute one.
- Where clinically meaningful, give the **number needed to treat (NNT)** (or number needed to harm).
- For safety, report **absolute event rates** by arm, not relative comparisons alone.

## Missing data, survival, and other essentials

- State the **amount and pattern of missing data** and the handling (e.g., multiple imputation); avoid naive last-observation-carried-forward as the primary approach.
- **Time-to-event**: Kaplan–Meier with numbers-at-risk; Cox model with the proportional-hazards assumption checked; report median follow-up.
- Pre-specify **interim analyses / stopping boundaries**; report them if a DSMB acted.
- For non-inferiority: state the pre-specified **margin** and its justification.

## Output format

```
【Per-outcome reporting】 effect + 95% CI present for primary + key secondary? gaps: [...]
【Primary analysis population】 ITT primary? per-protocol as sensitivity? yes/no
【Multiplicity】 hierarchy/adjustment pre-specified? exploratory endpoints labeled? yes/no
【Subgroups】 pre-specified? interaction tests reported? over-interpretation flags: [...]
【Absolute risk + NNT】 reported alongside relative measures? yes/no
【Missing data / survival / non-inferiority margin】 handled & stated? yes/no
【Causal language (observational)】 appropriately cautious? yes/no
【Next】 nejm-figures-tables
```

## Anti-patterns

- **Do not** report relative risk without absolute risk for clinical outcomes.
- **Do not** declare secondary or subgroup endpoints significant outside the multiplicity plan.
- **Do not** infer "no effect" from a wide CI crossing the null on an underpowered comparison.
- **Do not** use causal verbs ("reduced", "caused") for observational associations.
- **Do not** make per-protocol the primary analysis in a superiority trial.
