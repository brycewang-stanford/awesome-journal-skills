---
name: ecta-topic-selection
description: Use when judging whether a result is general, deep, and method-driven enough to belong in Econometrica, and when sharpening the contribution statement. Diagnoses fit and frames the contribution — it does not write proofs (use ecta-theory-model) or position against the literature (use ecta-literature-positioning).
---

# Topic Selection and Contribution Fit (ecta-topic-selection)

## When to trigger

- You have a model, an estimator, or a theorem but are unsure it clears the Econometrica bar
- The contribution reads like an application of a known method rather than a new method
- The result "works only for this example" and you suspect it needs more generality
- You cannot state the contribution in one sentence as a theorem or an estimator-plus-asymptotics

## What Econometrica rewards

Econometrica (Econometric Society / Wiley; founded 1933) is the field's flagship for
**econometric methods and rigorous economic theory**, not applied "top-5" causal-inference
papers. Its charter is the *unification of the theoretical-quantitative and the
empirical-quantitative approaches, penetrated by constructive and rigorous thinking*. It
prizes **generality and elegance over narrow application**; the product is a durable
methodological or theoretical advance. Before investing, classify the paper:

| Paper type | What must be true to fit | Exemplar |
|------------|--------------------------|----------|
| Econometric theory | A new estimator / test / identification result with full asymptotic theory and finite-sample evidence | Hansen (1982, GMM); Newey–West (1987, HAC) |
| Microeconomic / game theory | New axioms or a new model yielding existence/uniqueness, comparative statics, and an economic payoff | game-theoretic equilibrium-existence results |
| Decision theory | A representation theorem (axioms ⇔ functional form) with behavioral content | Kahneman–Tversky (1979, prospect theory) |
| Structural / empirical | A method or identification argument that is itself the contribution, applied with rigor | Rust (1987, nested fixed point); Heckman (1979, selection) |

A paper that is "policy evaluation with off-the-shelf DID/RDD" or "a clever application with
no new method" is off-fit, however well executed — redirect it to a general-interest applied
journal (AER / QJE / JPE / REStud). **This is the single most common Econometrica mismatch
and a desk-reject trigger**: at the eligibility/co-editor screen, "pure applied work lacking
a methodological or identification innovation" is routinely returned. The right question is
not "is this an important answer?" but "is the *estimator, theorem, or identification
argument* itself the contribution?"

## The generality test

Pressure-test the result before committing:

1. **Scope.** State the most general setting under which the result holds. If the proof
   only goes through for one parametric example, the contribution is an example, not a theorem.
2. **Necessity of assumptions.** For each assumption, ask: does the result fail without it?
   If an assumption is not used in the proof, drop it; if it is restrictive, justify it.
3. **Payoff.** What can a reader *do* with this that they could not before — estimate
   something previously inestimable, characterize behavior previously uncharacterized,
   weaken an assumption a classic result required?
4. **Depth vs. incremental.** Is this a genuinely new object/argument, or a marginal
   relaxation of a known theorem? Marginal relaxations need an outsized payoff to clear the bar.

## Contribution statement template

Write the contribution as 2–4 precise sentences, in the paper's own notation:

```
We study [setting / class of models]. We show that [central theorem: object, conditions,
conclusion]. Relative to [closest prior result], this [weakens assumption X / covers case Y
/ delivers the limiting distribution / characterizes the representation]. The result implies
[economic / inferential payoff].
```

Avoid "we propose a method and show it works." Name the theorem and the assumption it relaxes.

## Checklist

- [ ] Contribution stated as a theorem or estimator-plus-asymptotics, not as an application
- [ ] Most general setting identified; not tied to one parametric example
- [ ] Every assumption is used somewhere in the argument and is defensible
- [ ] Clear payoff: what becomes possible / characterizable that was not before
- [ ] Honest placement: is this Econometrica-deep (method/theorem), or general-interest-applied (AER/QJE/JPE/REStud)?
- [ ] The contribution survives the eligibility screen: a *new method/theorem/identification result*, not an off-the-shelf application
- [ ] A concrete behavioral or inferential consequence is stated, not just a formal property

## Anti-patterns

- A "method" that is a relabeling of an existing estimator with no new asymptotics
- Generality claimed in the intro but the proof only covers a single example
- An applied paper whose methodological contribution is thin, dressed up as a methods paper
- Assumptions stacked for convenience, several of them never used in any proof
- "Elegance" claimed with no comparison to the simpler existing result it supposedly beats

## Output format

```
【Paper type】econometric theory / micro-game-decision theory / structural-empirical
【Contribution (one sentence)】...
【Most general setting】...
【Closest prior result】...
【Payoff】...
【Fit verdict】Econometrica-fit / redirect to: ...
【Next step】ecta-literature-positioning
```
