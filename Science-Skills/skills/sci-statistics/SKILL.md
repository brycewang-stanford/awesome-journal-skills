---
name: sci-statistics
description: Use to enforce Science's statistics and reproducibility reporting — n and replication, test choice and assumptions, effect sizes with uncertainty, multiple-comparison control, randomization/blinding, and pre-registration where relevant.
---

# Statistics & Reproducibility (sci-statistics)

## When to trigger

- Results report P values but not effect sizes or n.
- "Three independent experiments" is claimed but replication is unclear.
- Multiple comparisons are run with no correction.
- A reviewer is likely to ask "were analyses pre-specified?" and there's no answer.

## The reporting backbone (every quantitative claim)

Each claim needs: **effect size + uncertainty + n + test + what n means.**

- [ ] **n** stated, with the unit of replication (biological vs technical replicates; cells vs animals vs experiments).
- [ ] **Effect size** with **95% CI** (preferred) or SD/SEM clearly labeled — not P alone.
- [ ] **Exact P values** (e.g., P = 0.013), not "P < 0.05", unless extremely small.
- [ ] **Test named and justified** (and its assumptions checked: normality, variance homogeneity, independence).
- [ ] **Multiple comparisons** corrected (Bonferroni/Holm/FDR) when many tests are run.

## Replication and design

- Distinguish **biological replication** (independent samples) from **technical replication** (re-measurement). Science cares about the former.
- State **how the sample size was chosen** (power analysis or rationale), not post-hoc.
- Report **randomization** of subjects/treatments and **blinding** of measurement/analysis where applicable, or state why not.
- Report **inclusion/exclusion criteria** and any data excluded, with reasons, decided in advance.

## Avoid the classic reviewer kills

- **Pseudoreplication**: treating technical replicates / cells from one animal as independent n.
- **HARKing / p-hacking**: presenting exploratory findings as confirmatory. If exploratory, label them.
- **"Representative" images** with no quantification across replicates.
- **Bar chart + SEM** masking a tiny, variable n.
- Comparing two effects by their **significance** ("significant here, not there") instead of testing the **difference**.

## Reproducibility package

- Analysis code in a repository (see `sci-data`), with a README and environment/versions.
- A reproducibility / reporting summary if requested by the journal — list software, versions, seeds.
- Deterministic where possible; report random seeds for simulations/ML.

## Pre-registration & transparency (where relevant)

- For confirmatory studies (especially with human subjects/behavioral work), note **pre-registration** (OSF/AsPredicted) if done.
- Separate pre-specified analyses from post-hoc exploration explicitly in the text.

## Output format

```
【Per-claim backbone】 effect+CI / n / unit-of-n / test / assumptions  → list gaps
【Replication】 biological vs technical clear? yes/no
【Sample-size rationale】 power/justification present? yes/no
【Randomization & blinding】 reported / N/A-justified / missing
【Multiplicity】 corrected? method
【Reproducibility】 code + versions + seeds present? yes/no
【Next】 sci-data
```

## Anti-patterns

- **Do not** report P without effect size and n.
- **Do not** count technical replicates as independent observations.
- **Do not** infer "no effect" from a non-significant test on an underpowered sample.
- **Do not** present post-hoc subgroup findings as if pre-specified.
