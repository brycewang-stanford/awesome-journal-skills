---
name: jf-workflow
description: Use when deciding which jf-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for The Journal of Finance (JF). Routes — it does not replace — the specialized skills.
---

# Workflow Router (jf-workflow)

## When to trigger

- You are unsure which `jf-*` skill applies to the current task
- You want an end-to-end sequence for a JF manuscript
- You are mid-project and need the next step

## What this pack targets

The Journal of Finance: AFA flagship, founded **1946**, bimonthly, Wiley-Blackwell, finance **top-3** with JFE and RFS, **~5% acceptance / ~33–45% desk reject** (afajof.org editor reports, accessed 2026-05-30). Distinctive JF mechanics this pack encodes: the **AFA online portal with a tiered submission fee** (high-income AFA member $400 / non-member $525; low-income $0), the **60-page limit** (≥1.5 spacing, 12-pt), the **Internet Appendix bundled at the end of the same PDF**, the **Data and Code Sharing Policy** with a **Data Editor**, and a **cover letter that is normally omitted**.

## End-to-end sequence

1. **`jf-topic-selection`** — is this general-interest and flagship-level?
2. **`jf-literature-positioning`** — state the marginal contribution; attribute canon to the right top-3 journal.
3. Design: **`jf-empirical-design`** (asset pricing) or **`jf-identification`** (corporate/causal).
4. **`jf-robustness`** — decisive checks in body, exhaustive battery + multiple-testing discipline in the Internet Appendix.
5. **`jf-tables-figures`** — self-contained exhibits, JF numbering, economic units.
6. **`jf-internet-appendix`** — allocate body vs. IA; keep body ≤60 pages.
7. **`jf-writing-style`** — general-interest intro; magnitude up front.
8. **`jf-referee-strategy`** — pre-empt objections; cover letter only for COI/code-exemption.
9. **`jf-submission`** — preflight: fee tier, 60-page check, bundled IA, code, disclosure.
10. **`jf-rebuttal`** — after an R&R, answer the editor first.

## Routing table

| Symptom                                   | Go to                         |
|-------------------------------------------|-------------------------------|
| "Is this big enough for JF?"              | `jf-topic-selection`          |
| "What's new vs. prior work?"              | `jf-literature-positioning`   |
| "How do I test this anomaly/factor?"      | `jf-empirical-design`         |
| "Is my causal claim identified?"          | `jf-identification`           |
| "Which robustness / multiple testing?"    | `jf-robustness`               |
| "Exhibits look amateur"                   | `jf-tables-figures`           |
| "Body too long / what goes online?"       | `jf-internet-appendix`        |
| "Intro buries the finding"                | `jf-writing-style`            |
| "What will referees attack?"              | `jf-referee-strategy`         |
| "Final pre-submit check / the fee"        | `jf-submission`               |
| "Got an R&R"                              | `jf-rebuttal`                 |

## Anti-patterns

- Jumping to `jf-submission` before fit and identification are settled
- Skipping `jf-internet-appendix` and breaching the 60-page limit
- Treating any single sub-skill as a substitute for the specialized ones

## Output format

```
【Current stage】...
【Recommended next skill】jf-...
【Why】...
```
