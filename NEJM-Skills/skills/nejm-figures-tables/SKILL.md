---
name: nejm-figures-tables
description: Use to build NEJM clinical display items correctly — Table 1 baseline characteristics by group (with standardized differences, not P values), Kaplan-Meier curves with numbers-at-risk, forest plots for subgroups and meta-analyses, and the CONSORT participant flow diagram.
---

# Clinical Display Items (nejm-figures-tables)

## When to trigger

- Table 1 reports P values comparing randomized groups (current guidance discourages this).
- A Kaplan–Meier plot has no numbers-at-risk row.
- Subgroup results are in text rather than a forest plot.
- The RCT lacks a CONSORT flow diagram, or its denominators don't reconcile.

## Table 1 — baseline characteristics by group

Table 1 describes the **baseline characteristics of the enrolled population, by group**.

- Columns are the randomized/study groups (and often an overall column); rows are characteristics (demographics, key clinical variables, disease severity).
- **Do not report P values comparing baseline characteristics in a randomized trial** — by design, baseline differences are due to chance. Current guidance is to report **standardized differences** if balance must be summarized.
- Report continuous variables as mean (SD) or median (IQR) per the distribution; categorical as n (%).
- Denominators must match the analysis populations and the CONSORT flow diagram.

## Kaplan–Meier curves (time-to-event)

- Show the survival/event curves per group over the follow-up period.
- **A numbers-at-risk row beneath the time axis is required** — readers must see how many remain at each time point.
- Consider showing the **hazard ratio with 95% CI** and the log-rank/Cox result on the panel.
- Censor marks or a clear censoring description; cumulative-incidence curves when competing risks matter.
- Do not extend curves into time ranges where almost no one remains at risk.

## Forest plots (subgroups & meta-analyses)

- For **subgroup analyses**: one row per pre-specified subgroup, the effect estimate with 95% CI, and the **interaction P value** (see `nejm-statistics`). A reference line at the null. Make clear which subgroups were pre-specified.
- For **meta-analyses**: per-study estimates with CIs, weights, the pooled estimate (diamond), and heterogeneity (I², τ²).
- Keep the scale honest (log scale for ratio measures); annotate which direction favors which arm.

## CONSORT participant flow diagram (RCTs)

The flow diagram is mandatory for trials (see `nejm-reporting`): Enrollment → Allocation → Follow-up → Analysis, with excluded/lost numbers and reasons at each stage. **Its numbers must reconcile** with Table 1 and the analysis populations.

## Figure specifications

- Legible at print size; sans-serif labels; avoid tiny fonts and hairlines.
- **Show uncertainty**: CIs on estimates, error bars defined in the legend, numbers-at-risk on K–M.
- Colorblind-safe palette; do not encode group by color alone (use line style/markers too).
- Each legend stands alone: what is shown, the groups, the statistic, n, and the error/CI definition.
- De-identify any patient images; remove protected health information from all panels (see `nejm-ethics`).

## Output format

```
【Table 1】 by group, n(%)/mean(SD)/median(IQR), NO baseline P values (standardized diffs ok)? yes/no
【Kaplan–Meier】 numbers-at-risk row present? HR+CI shown? censoring clear? yes/no
【Forest plot】 subgroups pre-specified + interaction P? / meta heterogeneity reported? yes/no
【CONSORT flow diagram】 present and reconciles with Table 1 + analysis n? yes/no
【Figure specs】 CIs shown / colorblind-safe / legends standalone / de-identified? yes/no
【Fixes】 [...]
【Next】 nejm-ethics
```

## Anti-patterns

- **Do not** put P values on baseline-comparison rows of Table 1 in a randomized trial.
- **Do not** show a Kaplan–Meier curve without a numbers-at-risk row.
- **Do not** bury subgroup results in prose — use a forest plot with interaction tests.
- **Do not** let the CONSORT flow numbers disagree with Table 1 or the analyzed populations.
- **Do not** display identifiable patient images or PHI.
