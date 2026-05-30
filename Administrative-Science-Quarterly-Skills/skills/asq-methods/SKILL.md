---
name: asq-methods
description: Use when choosing and justifying the research design for an Administrative Science Quarterly (ASQ) manuscript — qualitative (grounded-theory, ethnographic, historical) or quantitative — and setting the rigor bar. Designs the study; it does not run the analysis (see asq-data-analysis).
---

# Methods & Research Design (asq-methods)

## When to trigger

- You are deciding between a qualitative/inductive and a quantitative design
- Your design is chosen but its *rigor* and *transparency* are not yet defensible
- A qualitative study lacks theoretical sampling or trustworthiness safeguards
- A quantitative study lacks identification, or its design does not match the theory

## Principle: method follows the theoretical question

At ASQ, neither method is privileged. The journal publishes superb qualitative *and* quantitative work. What is non-negotiable is that the design fits the question (see `asq-theory-development`) and is executed with rigor. A sophisticated method cannot rescue a thin theory, and a simple design is fine if the insight is deep and the craft is high.

## Branch A — Qualitative / inductive design

Use for *how/why* process, emergence, meaning, identity, and contested dynamics.

Design requirements:

- **Theoretical (not convenience) sampling.** Cases/sites/informants selected to illuminate the construct or process; state the logic (polar types, theoretical replication, extreme/critical case, longitudinal).
- **Access and immersion.** Specify duration, depth, and your role (participant vs. non-participant); for ethnography, time in the field; for historical work, the archive.
- **Data sources, triangulated.** Interviews (count, who, when, semi-structured guide), observation, archival/internal documents, secondary sources — and how they corroborate.
- **Trustworthiness.** Address credibility, transferability, dependability, confirmability: member checks, prolonged engagement, audit trail, investigator triangulation, negative-case analysis.
- **Reflexivity.** Note your standpoint and how it shaped access and interpretation.

## Branch B — Quantitative design

Use for *whether/how much/under what conditions* questions across many cases.

Design requirements:

- **Sample and unit of analysis** justified relative to the theory (organizations, dyads, fields, events, individuals nested in units).
- **Identification.** Be explicit about the causal claim and the threat to it. Where causal language is used, justify it: panel FE, instruments, natural experiments, event-history/survival models, matching, difference-in-differences (and modern staggered-adoption caveats if relevant).
- **Measurement validity.** Construct operationalization defended; multi-item measures with reliability; address common-method bias if same-source.
- **Multilevel structure.** If theory is cross-level, use appropriate models (HLM/mixed models) and justify level of aggregation.
- **Power and design adequacy** for the effects and interactions claimed.

## Either branch

- The design must let you *see the mechanism*, not just the endpoints.
- Pre-empt the obvious alternative explanations at the design stage, not only in robustness.
- Plan the data-to-theory link now (this feeds `asq-data-analysis` and `asq-tables-figures`).

## Checklist

- [ ] Design matches the theoretical form (process → qualitative; variance → quantitative)
- [ ] Qualitative: theoretical sampling logic stated; access/immersion specified
- [ ] Qualitative: multiple triangulated data sources; trustworthiness safeguards named
- [ ] Quantitative: identification strategy explicit; causal claims justified
- [ ] Quantitative: measurement validity and (if needed) multilevel structure addressed
- [ ] Obvious alternative explanations are designed against, not just discussed
- [ ] The design can reveal the mechanism, not only the outcome

## Anti-patterns

- Convenience sampling dressed up as theoretical sampling
- Qualitative work with no transparency about coding, sources, or fieldwork depth
- Quantitative work asserting causality from cross-sectional, same-source data
- Choosing a fancy estimator/method to signal rigor when the question doesn't need it
- A design that can show *that* something happens but never *how/why* it happens

## Output format

```
【Design】qualitative (type) / quantitative (type)
【Why it fits】link to the theoretical question
【Sampling/identification】logic + key threat addressed
【Data sources】list + triangulation/measurement plan
【Rigor safeguards】trustworthiness or identification checks
【Next step】asq-data-analysis
```
