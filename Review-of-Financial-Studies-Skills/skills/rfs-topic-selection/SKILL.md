---
name: rfs-topic-selection
description: Use when the research question or contribution is the bottleneck for a The Review of Financial Studies (RFS) manuscript. Pressure-tests novelty-plus-rigor fit and drafts the contribution claim; does NOT design the empirics or position the literature in detail.
---

# Topic Selection & Novelty Fit (rfs-topic-selection)

## When to trigger

- The idea feels incremental, derivative, or "me-too"
- You can describe a method or dataset but not the *new question* it answers
- You are unsure whether the topic clears RFS's novelty bar (vs. a field journal)
- A coauthor says "this is clean but is it interesting enough for RFS?"

## The RFS fit test: novelty AND rigor

RFS prizes both. Score the idea on both axes before investing in empirics.

**Novelty axis — what is genuinely new?** At least one must be a strong "yes":
1. **New question** — a first-order finance question not previously framed this way.
2. **New mechanism / theory** — a model that reorganizes how we think about an old fact.
3. **New data** — a dataset that lets you see something previously invisible.
4. **New method** — a credibly better tool for an important question.

**Rigor axis — can it be established cleanly?** The answer must survive `rfs-identification` and `rfs-robustness`. Novelty without a credible research design is a desk-reject risk; rigor on a stale question is a field-journal paper.

**RFS-only consideration — the Registered Reports route.** RFS was the **first journal in finance/economics to offer Registered Reports** (pre-results review; G. Andrew Karolyi's 2014 editorial "Kick-Starting the Review Process," RFS 27(2)). If your question is important but the answer is genuinely uncertain — exactly the case where a "null" result would still be informative — consider the Registered Report path: the design is reviewed and granted **in-principle acceptance before results are known**, removing the incentive to manufacture significance. This is a topic-selection lever JF and JFE do not offer. A question whose value depends on the sign of the result is a weak Registered Report; a question whose value holds regardless of the answer is ideal.

## RFS-favored frontiers (durable, verify current calls for papers)

RFS has been notably open to:
- **Intermediary asset pricing & liquidity spirals** — balance-sheet constraints, dealers, funding. RFS published the canonical Brunnermeier–Pedersen (2009) "Market Liquidity and Funding Liquidity" (RFS 22(6)).
- **Cross-sectional asset pricing & anomaly digestion** — e.g., Hou, Xue, and Zhang (2015) "Digesting Anomalies: An Investment Approach" (RFS 28(3), the q-factor model) and Bollerslev, Tauchen, and Zhou (2009) "Expected Stock Returns and Variance Risk Premia" (RFS 22(11)).
- **Fintech / digital finance** — platforms, marketplace lending, crypto market microstructure, AI in finance.
- **Climate / sustainable finance** — physical and transition risk, ESG pricing, green capital allocation.
- **Household & behavioral finance** — consumption, mortgages, retail investors, belief formation.
- **Theory tightly integrated with empirics** — RFS welcomes structural and model-driven papers, not just reduced-form.

This is a durable orientation, not a fixed list. Check the RFS site for current special issues, Registered Report calls, and editor priorities before anchoring a framing on them.

## Contribution claim template

Draft three to five explicit contribution sentences for the introduction:

1. **The question**: "We ask whether / how [X affects Y] in [setting]." (Make the novelty visible here.)
2. **The wedge**: "Prior work [Author, year] established [A] but could not [B] because [data/identification gap]."
3. **What we do**: "Using [new data / new design / new model], we [show / estimate / prove] ..."
4. **What we find**: "[Quantified result with magnitude], robust to [...]."
5. **Why it matters**: "This changes how we think about [theory / policy / practice]."

## Checklist

- [ ] At least one novelty axis is a strong "yes," stated in one sentence
- [ ] The question is first-order for finance, not a narrow sub-case
- [ ] A credible identification or asset-pricing strategy exists (sketch it now)
- [ ] The contribution is *not* "we re-run a known design on a new sample"
- [ ] Theory and empirics are mutually reinforcing, not bolted together
- [ ] You can name the 2–3 RFS/JF/JFE papers this most directly extends or overturns
- [ ] If the answer's value does not hinge on its sign, the Registered Report route was considered

## Anti-patterns

- A clean but stale question — survives rigor, fails novelty ("me-too" paper).
- A flashy new dataset with no question — novelty as decoration.
- Over-claiming a "new method" that is a minor variant of an existing estimator.
- Hiding the contribution behind data description.
- Chasing a trendy frontier (e.g. crypto) without a finance question that matters.

## Output format

```
【Question】one-sentence new question
【Novelty axis】new-question / new-mechanism / new-data / new-method (which + why)
【Closest prior work】[Author year @ JF/JFE/RFS] → our delta
【Rigor sketch】likely identification / asset-pricing strategy
【Registered Report?】value independent of result sign → consider Stage 1 route
【RFS fit verdict】strong / borderline / field-journal
【Next step】rfs-literature-positioning
```
