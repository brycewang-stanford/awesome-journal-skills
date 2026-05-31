---
name: jf-robustness
description: Use when planning or auditing the robustness, sensitivity, and multiple-testing battery for a The Journal of Finance (JF) manuscript. Decides which checks are load-bearing; it does not design the main test.
---

# Robustness & Multiple Testing (jf-robustness)

## When to trigger

- The main result is in; you must decide which robustness checks to run and where to put them
- A referee will ask "does it survive [alternative measure / subsample / specification]?"
- The finding is one of many you tested and multiple testing is a live concern

## JF norm: decisive in the body, exhaustive in the Internet Appendix

JF favors an accessible body within the **60-page limit**. Put the **3–6 decisive checks** in the main text and move the exhaustive battery to the **Internet Appendix**, which is **bundled at the end of the same PDF** and **does not count toward 60 pages** (see `jf-internet-appendix`). This main-text/IA split is a JF hallmark; do not bury a load-bearing check.

## Multiple testing — a JF-salient concern

JF published the canonical "factor zoo" critique (**Harvey, Liu & Zhu, "…and the Cross-Section of Expected Returns," JF**). Reviewers therefore expect:
- An honest account of **how many specifications/signals were tried**.
- **Adjusted thresholds** (e.g., higher t-cutoffs, FDR control) for any discovery mined from many candidates, not the naive 1.96.
- Pre-registration-style discipline in framing (no HARKing).

## Robustness battery (select the load-bearing ones for the body)

- Alternative measures of the key variable
- Subsamples (time, size, industry) and the obvious excluded-period test
- Alternative standard errors / clustering dimensions
- Alternative controls / fixed effects; placebo and falsification tests
- For asset pricing: alternative factor models and EIV-corrected SEs (see `jf-empirical-design`)

## Checklist

- [ ] 3–6 decisive checks in the body; the rest in the Internet Appendix
- [ ] Number of specifications tried is disclosed
- [ ] Multiple-testing adjustment applied to mined results
- [ ] At least one placebo/falsification test
- [ ] No load-bearing robustness check hidden in the appendix
- [ ] Body stays within 60 pages after the split

## Anti-patterns

- A 20-table robustness section in the body that pushes the paper over 60 pages
- Reporting only the specifications that "work" without disclosing the search
- Treating raw t > 1.96 as decisive after extensive mining
- Hiding the one check that actually threatens the result in the Internet Appendix

## Output format

```
【Decisive checks in body】[3–6]
【Specifications tried disclosed?】yes / no
【Multiple-testing adjustment?】yes / no — method
【Placebo/falsification present?】yes / no
【Body ≤60 pp after split?】yes / no
【Next step】jf-tables-figures
```
