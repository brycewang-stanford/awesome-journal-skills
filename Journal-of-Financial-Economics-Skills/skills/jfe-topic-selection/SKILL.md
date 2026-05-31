---
name: jfe-topic-selection
description: Use when scoping or framing a topic for a Journal of Financial Economics (JFE) manuscript and you need to test fit and contribution before investing in data work. Pressure-tests the question and contribution; it does not write the literature review or design the empirics.
---

# Topic Selection & Fit (jfe-topic-selection)

## When to trigger

- You have data or a setting but no sharp economic question yet
- You are unsure whether the idea clears the JFE contribution bar
- You cannot state in one sentence what is new relative to existing finance papers
- You are choosing between JFE, JF, and RFS as the target outlet

## What JFE rewards

JFE (Elsevier; North-Holland; ISSN 0304-405X; founded 1974 by Michael C. Jensen) is one of the top-3 finance journals and publishes rigorous, methodologically demanding **empirical** corporate finance and asset pricing, plus the financial-economics theory that supports them. Its stated scope centers on **capital markets, financial institutions, corporate finance, corporate governance, and the economics of organizations**. The durable preference: a clean economic question, answered with a credible design and exhaustive evidence.

The two JFE best-paper prizes signal the two halves of the journal's taste: the **Jensen Prize** (best corporate-finance / organizations paper) and the **Fama-DFA Prize** (best asset-pricing / capital-markets paper). Aim a JFE submission at the kind of paper that could plausibly compete for one of them. (Editor-in-Chief Toni M. Whited, Michigan, since 2021; verify current scope on jfinec.com.)

Fit test — answer all four before proceeding:

1. **Economic question.** Is there a real financial-economics question, not just a correlation you can run? "Does X cause Y, and through what channel?" beats "X is associated with Y."
2. **Contribution.** Can you name the specific result that is new — a new fact, a new mechanism, a new identification, or overturning a believed result? Incremental "X in a new sample" rarely clears the bar.
3. **Credible answer.** Is there a plausible path to identification or to disciplined inference (see `jfe-identification`, `jfe-empirical-design`)? If the honest answer is "OLS with controls," the topic is not ready.
4. **Depth.** Can the result survive the robustness and referee culture JFE is known for? If one alternative explanation sinks it, reconsider.

## Contribution framing (draft early, refine often)

State the contribution as 2–4 explicit sentences for the introduction:

- **The gap:** what the literature currently believes or has not established.
- **The move:** the setting, design, or data that lets you resolve it credibly.
- **The finding:** the headline result, with direction and rough magnitude.
- **Why it matters:** for theory, for other empirical work, or for policy/practice.

## Corporate finance vs. asset pricing framing

- **Corporate finance (Jensen-Prize territory):** lead with the causal question and the identifying variation (a shock, a discontinuity, an instrument). The contribution is usually "credible causal effect of X on corporate outcome Y, plus mechanism." The agency-cost lens of **Jensen & Meckling (1976, JFE)** is the lineage your governance/financing question sits in.
- **Asset pricing (Fama-DFA territory):** lead with the economic source of the return pattern and how you discipline inference. The contribution is usually "a return predictor/factor that is real after correct standard errors, out-of-sample, and multiple-testing scrutiny," or a mechanism for a known anomaly. The factor-model tradition of **Fama & French (1993, JFE)** and **Banz (1981, JFE, the size effect)** sets the bar a new factor must clear.

> Reminder: a famous result is not automatically a JFE result. **Carhart (1997)** momentum-persistence is a *Journal of Finance* paper, not JFE — do not position against it as if it were the JFE house lineage.

## Checklist

- [ ] One-sentence economic question written down
- [ ] Headline contribution stated in 2–4 sentences (gap / move / finding / why)
- [ ] Named the closest 3–5 papers this would sit beside and how it differs
- [ ] Plausible identification or inference path exists (not "OLS + controls")
- [ ] The result would survive an exhaustive robustness battery
- [ ] The paper could credibly compete in its Jensen-Prize (corp fin) or Fama-DFA (asset pricing) lane
- [ ] Honest read on whether JFE, JF, or RFS is the best home — and worth the non-refundable US$850 submission fee

## Anti-patterns

- A "kitchen-sink regression" with no economic question behind it
- "First paper to study X in country/sample Z" with no methodological or conceptual advance
- A correlation dressed as a finding, with identification deferred to "future work"
- An asset-pricing predictor pitched without any awareness of multiple-testing concerns
- Picking JFE because it is prestigious rather than because the design depth fits

## Output format

```
【Question】one-sentence economic question
【Contribution】gap / move / finding / why-it-matters
【Field】corporate finance | asset pricing | financial-economics theory
【Closest papers】[...] and how this differs
【Identification path】sketch (or "not yet — see jfe-identification")
【Fit verdict】JFE | JF | RFS | not ready
【Next】jfe-literature-positioning
```
