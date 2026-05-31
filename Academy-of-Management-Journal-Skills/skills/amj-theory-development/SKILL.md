---
name: amj-theory-development
description: Use when the theoretical argument and hypotheses are the bottleneck for an Academy of Management Journal (AMJ) manuscript — building a mechanism and deriving testable hypotheses a priori. Constructs the theory; it does not run the analysis (amj-data-analysis) or write the final contribution paragraph (amj-contribution-framing).
---

# Theory Development & Hypotheses (amj-theory-development)

## When to trigger

- Hypotheses read as bald predictions ("A is positively related to B") with no mechanism
- You have results and are tempted to write hypotheses around them (HARKing risk)
- The argument leans on one borrowed citation rather than a developed logic
- Mediators/moderators are present in the data but not theorized
- A reviewer says "the theory is thin," "the logic is underdeveloped," or "why would this be true?"

## The AMJ theory bar

AMJ does not publish atheoretical work — its mission is "to publish empirical research that tests, extends, or builds management theory." Every hypothesis must be **derived from an articulated theoretical mechanism**, written *before* the results are known. The argument should make a reader feel they understand *why* the effect occurs and *under what conditions* it strengthens or reverses.

For **theory-building** (typically qualitative) papers, AMJ does *not* expect a priori hypotheses; it expects a grounded model with emergent propositions. Eisenhardt and Graebner's AMJ guidance on building theory from cases is the canonical exemplar for how rich data become crisp constructs and propositions — do not force such a study into a hypothetico-deductive template.

## Building a hypothesis (the mechanism chain)

For each hypothesis, write the explicit chain — do not skip steps:

1. **Antecedent** — the predictor and why it matters in this context.
2. **Mechanism** — the theoretical process linking antecedent to outcome (e.g., social exchange, signaling, attention allocation, identity threat, resource dependence). Name the theory and the process verb (motivates, signals, depletes, legitimates).
3. **Outcome** — the dependent construct, defined at a stated level of analysis.
4. **Direction & form** — sign, and whether linear, curvilinear, or threshold.
5. **Boundary** — the moderator(s) and the theoretical reason the mechanism is stronger/weaker.

State the level of analysis explicitly (individual, team, firm) and keep the theory at the level where the mechanism operates; flag cross-level mediation as such.

## Mediation and moderation done right

- **Mediation**: theorize the *process* construct before testing it; do not infer the mechanism from a significant indirect effect alone. An indirect effect is evidence *for* a theorized mechanism, not a substitute for the theory.
- **Moderation**: give a substantive reason the slope changes — "it depends on" is not a theory until you say *why* it depends.
- **Curvilinear**: justify the turning point theoretically (two opposing forces), not just by a significant squared term.

## Hypothesis hygiene

- Number hypotheses and keep them to a defensible set (typically a focal effect plus a mechanism and one or two boundaries). Avoid a "kitchen sink" of ten weakly motivated predictions.
- Each hypothesis must be falsifiable and tied to a specific test you will run.
- Competing/alternative theoretical explanations should be named and addressed, not ignored.
- A figure of the theoretical model (boxes and arrows) should map one-to-one to the hypotheses.

## Checklist

- [ ] Every hypothesis has an explicit mechanism, not just a predicted sign
- [ ] The driving theory is named and its process clearly invoked (not a one-line citation)
- [ ] Level of analysis is stated and consistent across argument and design
- [ ] Mediators/moderators are theorized a priori with substantive reasons
- [ ] Hypotheses were derived before analyzing the data (no HARKing)
- [ ] A theoretical-model figure matches the hypotheses exactly
- [ ] At least one rival explanation is named and engaged

## Anti-patterns

- **HARKing**: hypothesizing after results are known; reviewers detect it when every hypothesis is supported and none is surprising.
- **Bald predictions**: "We hypothesize A is positively related to B" with no *why*.
- **Borrowed theory**: invoking a famous theory by name without using its actual logic.
- **Mechanism by mediation**: claiming a process exists only because the indirect effect is significant.
- **Kitchen-sink hypotheses**: many predictions, each thinly argued, that no single theory ties together.
- **Boundary without reason**: a moderator with no theoretical account of why the effect should differ.

## Output format

```
【Focal theory】... (process verb: ...)
【H1 (focal effect)】antecedent → mechanism → outcome; direction/form; level
【H2 (mechanism/mediation)】...
【H3+ (boundary/moderation)】... reason the slope changes
【Rival explanation addressed】...
【HARKing check】hypotheses fixed before analysis? yes/no
【Model figure】matches hypotheses one-to-one? yes/no
【Next step】amj-literature-positioning, then amj-methods
```
