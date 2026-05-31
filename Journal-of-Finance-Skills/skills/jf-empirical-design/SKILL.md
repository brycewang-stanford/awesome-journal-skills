---
name: jf-empirical-design
description: Use when designing or stress-testing an asset-pricing test for a The Journal of Finance (JF) manuscript — factor models, Fama–MacBeth vs. panel, standard-error corrections, out-of-sample discipline. For corporate causal claims use jf-identification.
---

# Asset-Pricing Test Design (jf-empirical-design)

## When to trigger

- You have a candidate predictor / anomaly / factor and must decide how to test it
- You are unsure whether to run Fama–MacBeth, time-series factor regressions, or a panel
- You report t-stats but have not addressed the standard-error subtleties of cross-sectional asset pricing
- A referee will ask "is this data mining / does it survive multiple testing / does it work out of sample?"

> Scope: this skill is for **asset-pricing tests**. For corporate/empirical causal effects, route to `jf-identification`.

## Choosing the test

| Goal                                            | Workhorse design                                            |
|-------------------------------------------------|-------------------------------------------------------------|
| Does characteristic X price the cross-section?  | Fama–MacBeth cross-sectional regressions + portfolio sorts  |
| Is a candidate factor priced / spanned?         | Time-series regressions; GRS test; spanning vs. established factors |
| Compare competing factor models                 | Alphas of test assets; max-Sharpe / HJ distance; model comparison |
| Does a signal predict returns?                  | Predictive regressions + long-short; in/out-of-sample R² (Campbell–Thompson) |
| Panel with firm/time variation                  | Panel with appropriate fixed effects and clustering         |

## JF-specific standards

JF asset-pricing referees engage the JF-published canon — **Sharpe (1964) CAPM, Fama–French (1992), Jegadeesh–Titman (1993) momentum, Carhart (1997)** — and expect you to benchmark against the right factors (recall the FF three-factor model is JFE 1993). They also expect:
- **Errors-in-variables / Shanken correction** on Fama–MacBeth standard errors where betas are estimated.
- **Multiple-testing discipline**: a new anomaly must survive the "factor zoo" critique (Harvey, Liu & Zhu, JF) — adjusted t-thresholds, not the naive 1.96.
- **Out-of-sample** evidence for predictability claims, not just in-sample fit.
- **Economic magnitude** (Sharpe gain, alpha in bps), since JF writes for a general-interest reader.
- Exhaustive specifications go to the **Internet Appendix** (bundled in the same PDF; see `jf-internet-appendix`), keeping the body within 60 pages.

## Checklist

- [ ] Test matched to the question (FM / time-series / panel)
- [ ] Standard errors correct for the design (Shanken, NW, clustering)
- [ ] New factor/anomaly survives a multiple-testing-adjusted threshold
- [ ] Out-of-sample check for any predictability claim
- [ ] Benchmarked against the standard factor models, attributed correctly
- [ ] Economic magnitude reported, not just t-stats

## Anti-patterns

- Reporting raw t > 1.96 as decisive after mining many signals (the factor-zoo trap)
- Fama–MacBeth t-stats with no EIV/Shanken adjustment
- In-sample-only predictability dressed up as a discovery
- Crowding every robustness table into the body instead of the Internet Appendix

## Output format

```
【Test chosen + why】...
【SE correction (Shanken/NW/cluster)】...
【Multiple-testing threshold cleared?】yes / no
【Out-of-sample evidence?】yes / no
【Economic magnitude】...
【Next step】jf-robustness
```
