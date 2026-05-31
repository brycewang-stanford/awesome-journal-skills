---
name: smj-theory-development
description: Use when building the theoretical mechanism and hypotheses for a Strategic Management Journal (SMJ) manuscript. Constructs the argument and develops hypotheses; it does not position the literature or run estimation.
---

# Theory Development & Hypotheses (smj-theory-development)

## When to trigger

- Your hypotheses read as signed predictions ("X is positively related to Y") with no logical engine
- The theory section restates prior findings instead of building a new argument
- A moderator is added but you cannot explain *why* it changes the effect
- The mechanism connecting strategic choice to performance is implicit or hand-waved

## What SMJ means by "theory"

SMJ wants a **causal logic**: a chain of premises that explains *why* a strategic choice or condition produces a performance/advantage consequence, anchored in a recognized strategy perspective. A hypothesis without a stated mechanism is a correlation in disguise. The reviewers expect you to show the logical steps, not just the conclusion.

## Choosing and combining lenses

| Lens                          | Core engine                                            | Typical use |
|-------------------------------|--------------------------------------------------------|-------------|
| Resource-based / capabilities | Heterogeneous, hard-to-imitate resources earn rents (Wernerfelt, 1984, SMJ) | Why advantage persists |
| Dynamic capabilities          | Sensing/seizing/reconfiguring under change (Teece, Pisano & Shuen, 1997, SMJ) | Adaptation, renewal |
| Transaction cost economics    | Governance minimizes contracting hazards               | Make-vs-buy, alliances, scope |
| Agency / governance           | Incentive misalignment shapes strategic choice         | Boards, ownership, M&A |
| Competitive dynamics          | Action–response, awareness–motivation–capability       | Rivalry, market entry |
| Behavioral theory of the firm | Aspirations, search, attention                         | Risk taking, R&D search |
| Real options                  | Sequential investment under uncertainty                | Entry, staging, divestiture |
| Institutional / nonmarket     | Legitimacy and regulatory environment shape advantage  | CSR, political strategy |

Borrowing a lens is fine; **extending or qualifying** it is what earns a contribution. State which lens you build on and exactly where you depart from it.

> Anchor RBV with **Wernerfelt (1984), SMJ** when you want an SMJ-internal reference. Barney's much-cited 1991 RBV statement appeared in *Journal of Management*, **not** SMJ — do not list it as an SMJ landmark.

SMJ is a **theory-develop-and/or-test** journal: unlike AMR, it does not publish purely conceptual papers, so your theory must set up implications that are evaluable (testable, or otherwise assessable for qualitative/formal work).

## Building the argument (mechanism-first)

1. **Establish the baseline relationship.** State the focal X → Y and the strategy logic for its sign.
2. **Specify the mechanism.** Name the mediating process (e.g., reduced imitation, lower coordination cost, shifted aspirations). The mechanism is the contribution's spine.
3. **Develop moderators as theory, not robustness.** A moderator hypothesis must explain how the boundary condition *strengthens or reverses the mechanism* — not merely "the effect is bigger for big firms."
4. **Surface and address the tension.** SMJ rewards arguments that resolve a real tension or counter-prediction (e.g., a resource that both enables and constrains).
5. **State the counterfactual and scope conditions.** Where does the logic hold, and where does it break?

## Hypothesis craft

- Each H states direction *and* carries a one-line mechanism in the surrounding text.
- Order hypotheses so the baseline (H1) precedes mediation/moderation (H2, H3…).
- Avoid "kitchen-sink" hypothesizing; 2–4 tightly linked hypotheses beat seven loose ones.
- If you theorize a mediator, plan a mechanism test in `smj-data-analysis` (mediation alone is weak evidence).

## Checklist

- [ ] Every hypothesis is preceded by an explicit causal mechanism
- [ ] You name the lens you extend and the specific gap/tension you resolve
- [ ] Moderators are theorized (why the mechanism shifts), not bolted on
- [ ] A counter-argument / competing prediction is acknowledged and addressed
- [ ] Scope and boundary conditions are stated
- [ ] The argument predicts something a reader could not already infer from prior work

## Anti-patterns

- "X is positively associated with Y" with no mechanism — the most common SMJ theory weakness
- Hypothesis salad: many predictions, no integrating logic
- Re-deriving an established result and calling it theory
- A moderator with no theoretical reason for changing the effect
- Mechanism claimed in theory but never tested empirically
- Using a strategy lens as decoration while the real argument is generic

## Output format

```
【Lens】RBV | dynamic capabilities | TCE | agency | competitive dynamics | BTOF | real options | institutional
【Gap/tension resolved】...
【Mechanism (one sentence)】X affects Y because ...
【Hypotheses】H1 (baseline) / H2 (mediation) / H3 (moderation) — each with its mechanism
【Boundary conditions】...
【Empirical implication】mechanism test needed → flag for smj-data-analysis
【Next step】smj-literature-positioning
```

## Templates & resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ scope and verified landmark strategy-theory papers (Wernerfelt 1984; Teece, Pisano & Shuen 1997)
