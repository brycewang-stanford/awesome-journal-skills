---
name: qje-theory-model
description: Use when a Quarterly Journal of Economics (QJE) manuscript has a credible empirical result but no conceptual frame — to add the model or framework that turns a coefficient into a lesson. Frames the result conceptually; it does not redesign the identification.
---

# Theory & Conceptual Frame (qje-theory-model)

## When to trigger

- The empirics are clean but the paper reads as "a coefficient with no story"
- Referees would ask "what is the economic mechanism / model behind this?"
- There is a verbal mechanism but no formalization tying estimates to parameters
- The result is interesting but its broad implication is not articulated

## Why QJE wants a frame, not necessarily heavy theory

QJE rewards a **clear conceptual takeaway with broad implications**. That does not mean every paper needs a structural model — many of the journal's most influential empirical-micro papers carry a *light* conceptual framework whose role is to (1) organize what is being estimated, (2) make the mechanism legible, and (3) map reduced-form estimates to an economically meaningful quantity. Match the weight of theory to the question; do not bolt on a model that the empirics cannot speak to.

## Choosing the right level of formalization

| Level                        | Use when...                                                        | Risk if misused                          |
|------------------------------|--------------------------------------------------------------------|------------------------------------------|
| Verbal conceptual frame      | The mechanism is intuitive and the estimate is the contribution    | Reads as undertheorized; "so what?"      |
| Stylized model (1–3 results) | You need to show *what parameter* the design identifies            | Best default for empirical-micro QJE     |
| Sufficient-statistic frame   | A few estimable objects map to welfare/policy                      | Powerful and parsimonious when it fits   |
| Full structural model        | Counterfactuals/welfare require out-of-sample extrapolation        | Overkill if the question is a clean ATT  |

## The framing moves

1. **Define the object.** State precisely what economic quantity the empirical estimate corresponds to (an elasticity, a treatment effect on a welfare-relevant margin, a structural parameter).
2. **Make the mechanism a proposition.** Even a two-equation model that yields "the sign/size of β reveals mechanism M" disciplines the interpretation and tells referees what the test is.
3. **Connect to welfare or policy.** Where possible, use a sufficient-statistic or envelope argument to translate estimates into a quantity decision-makers care about.
4. **State the broad lesson.** Close the loop with the topic-selection hook: the model should make the "beyond this setting" sentence rigorous.

## Checklist

- [ ] The estimated object is defined in terms of an economic primitive
- [ ] The model (verbal or formal) generates a testable prediction the data address
- [ ] Theory weight is matched to the question (no gratuitous structural model)
- [ ] Mapping from reduced-form estimates to the conceptual quantity is explicit
- [ ] A welfare / policy interpretation is offered where feasible
- [ ] The frame makes the "broad lesson" rigorous, not decorative
- [ ] Assumptions of the frame are stated and their plausibility discussed

## Anti-patterns

- A standalone theory section disconnected from what the data can test
- A structural model whose key parameters the design cannot identify
- "Mechanism" asserted verbally with no prediction that the empirics confirm/reject
- Theory that merely restates the regression rather than disciplining it
- A model so general it predicts any sign of the estimate (unfalsifiable)

## Output format

```
【Estimated object】what economic primitive the coefficient maps to
【Frame level】verbal / stylized model / sufficient-statistic / structural
【Key prediction】the testable implication the data address
【Welfare/policy mapping】... (or "not applicable, by design")
【Broad lesson, made rigorous】...
【Next step】qje-robustness
```
