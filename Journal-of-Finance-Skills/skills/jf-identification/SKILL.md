---
name: jf-identification
description: Use when the causal-identification strategy is the bottleneck for a corporate / empirical The Journal of Finance (JF) manuscript — natural experiments, IV, DID, RDD. Stress-tests the design; for asset-pricing tests use jf-empirical-design.
---

# Causal Identification (jf-identification)

## When to trigger

- The paper makes a causal claim ("X causes Y") resting on a research design
- You rely on an instrument, a shock, a discontinuity, or a diff-in-diff and a referee will attack the exclusion/parallel-trends assumption
- Endogeneity (reverse causality, omitted variables, selection) threatens the headline result

> Scope: corporate / empirical causal effects. For cross-sectional asset-pricing tests use `jf-empirical-design`.

## JF's bar for identification

JF is the AFA flagship, general-interest, with a ~5% acceptance rate and ~33–45% desk rejection (afajof.org editor reports, accessed 2026-05-30). For a corporate/empirical paper, **credible identification is usually the binding constraint** — a clever question with a weak design is a classic JF desk reject. The design must convince a broad AFA readership, not just specialists.

## Design audit

| Design                 | Core assumption to defend                     | Standard JF attack to pre-empt                 |
|------------------------|-----------------------------------------------|------------------------------------------------|
| Natural experiment     | Shock is plausibly exogenous & well-timed     | Anticipation; confounding co-occurring events  |
| Instrumental variables | Relevance + exclusion                         | "Why does the instrument affect Y only via X?" |
| Diff-in-diff           | Parallel trends; no differential shocks       | Pre-trends; staggered-adoption bias            |
| RDD                    | No manipulation; continuity at the cutoff     | Bunching; bandwidth sensitivity                |

- State the **source of variation** in one sentence in the introduction (JF rewards a clearly named shock or instrument).
- Show the **identifying assumption** is testable where possible (pre-trends, first-stage F, McCrary test) and put the full battery in the **Internet Appendix** (bundled in the same PDF; see `jf-internet-appendix`).
- Report **economic magnitude**, since JF writes for a general-interest reader.

## Checklist

- [ ] Source of identifying variation named in one sentence
- [ ] Exclusion / parallel-trends / continuity assumption explicitly defended
- [ ] First-stage strength (IV) or pre-trend evidence (DID) shown
- [ ] Modern estimators used where staggered adoption applies
- [ ] Confounders and anticipation effects addressed
- [ ] Magnitude interpreted, not just significance

## Anti-patterns

- A causal verb ("increases", "causes") with only conditional correlations behind it
- An instrument with a hand-waved exclusion restriction
- Two-way fixed-effects DID on staggered adoption with no modern correction
- A clever question whose design no broad-readership editor would send out

## Output format

```
【Design】NE / IV / DID / RDD
【Source of variation (1 sentence)】...
【Key assumption + how defended】...
【Main threat pre-empted?】yes / no
【Magnitude】...
【Next step】jf-robustness
```
