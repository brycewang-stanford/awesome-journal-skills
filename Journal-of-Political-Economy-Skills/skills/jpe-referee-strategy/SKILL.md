---
name: jpe-referee-strategy
description: Use when running a pre-submission pre-mortem on a Journal of Political Economy (JPE) manuscript to anticipate the price-theory, general-equilibrium, and identification objections a Chicago referee will raise. Builds the threat list and pre-empts it; it does not write the R&R response (see jpe-rebuttal).
---

# Referee Strategy & Pre-Mortem (jpe-referee-strategy)

## When to trigger

- Identification, model, and robustness are in place and you want to harden the paper before submitting
- You want to anticipate the report rather than react to it
- You sense a likely objection but have not addressed it in the text
- You are choosing how to frame the contribution to survive a demanding economics referee

## How JPE referees read

JPE referees read the paper as an **economic argument** and probe its internal consistency. The prototypical Chicago referee asks: does this respect optimization, prices, incentives, and equilibrium? They are unimpressed by a clean coefficient with no economic meaning, and they will name the alternative mechanism or the GE force you ignored. Anticipating these is worth more than any extra robustness table. The process is selective and demanding; a single unanswered first-order objection sinks a paper.

## The objection taxonomy (pre-empt each in the text)

1. **"Where is the economics?"** — A reduced-form result with no model/mechanism. *Pre-empt:* `jpe-theory-model` — state the mechanism and the prediction it tests.
2. **"This ignores general equilibrium."** — A partial effect that nets out when prices/quantities adjust. *Pre-empt:* address GE feedback; bound or sign the equilibrium effect.
3. **"Your mechanism vs. the obvious alternative."** — A rival economic story produces the same sign. *Pre-empt:* `jpe-robustness` — a discriminating test.
4. **"Selection / endogeneity."** — Treatment or sample is endogenous. *Pre-empt:* `jpe-identification` — defend the assumption, show falsification.
5. **"What identifies the parameter?"** (structural) — *Pre-empt:* explicit "what identifies what" + untargeted-moment validation.
6. **"So what?"** — credible but unimportant. *Pre-empt:* `jpe-topic-selection` — state the portable lesson and magnitude.
7. **"Internal inconsistency."** — the model's assumption contradicts the empirical setting, or two claims conflict. *Pre-empt:* a consistency pass across model, data, and conclusion.

## Pre-mortem procedure

- Write the referee report you fear, in their voice, listing the three objections most likely to trigger a reject.
- For each, decide: fixable in text now (do it), needs new analysis (do it or scope it), or a genuine limitation (state it honestly and bound its damage).
- Identify the **one** first-order objection that would sink the paper and make sure the manuscript answers it before a referee has to ask.
- Suggesting referees / handling COIs: name scholars who know the literature and would engage fairly; note conflicts honestly.

## Checklist

- [ ] "Where is the economics?" answered by an explicit mechanism/model
- [ ] General-equilibrium feedback addressed or bounded
- [ ] The leading rival mechanism named and tested against
- [ ] Selection/endogeneity threat defended with a falsification test
- [ ] (Structural) parameter identification made transparent
- [ ] Importance / portable lesson stated, not assumed
- [ ] Model–data–conclusion consistency pass done
- [ ] The single most dangerous objection identified and pre-empted in the text

## Anti-patterns

- Submitting with an obvious GE or selection objection unaddressed, hoping the referee misses it
- A robustness section that never tests the *leading* rival mechanism
- Assuming importance instead of demonstrating it
- Hiding a known limitation rather than bounding it (referees find it anyway)
- Treating the pre-mortem as optional polish rather than the cheapest way to avoid a reject

## Output format

```
【Feared report】the 3 objections most likely to trigger reject
【First-order threat】the single objection that would sink it
【Pre-empt plan】per objection: fix-in-text / new-analysis / state-as-limitation
【GE + rival-mechanism status】addressed? [y/n]
【Consistency pass】model–data–conclusion coherent? [y/n]
【Next】jpe-submission
```
