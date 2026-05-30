---
name: amr-theory-development
description: Use when building the actual theory for an Academy of Management Review (AMR) manuscript — turning a positioned puzzle into defined constructs, explicit relationships, propositions, and boundary conditions. Constructs the theory; it does NOT stress-test the argument's logic (that is amr-data-analysis) or design any data collection (AMR has none).
---

# Theory Development: Constructs, Relationships, Propositions (amr-theory-development)

## When to trigger

- The puzzle and conversation are set; now you must build the theory
- You have propositions but no defined constructs underneath them
- Your relationships are asserted, not derived
- You have not stated boundary conditions or assumptions

## The build order

AMR theory is assembled in a disciplined sequence. Skipping a step is the most common
reason a draft reads as "assertions, not theory."

1. **Define the constructs.** For each new or re-specified construct: a precise conceptual
   definition, its **domain** (what it includes and, crucially, excludes), and how it
   differs from neighboring constructs. A construct that overlaps an existing one without
   distinction will be challenged.
2. **State the assumptions.** What must be true about actors, the setting, and the world
   for the theory to operate? Make them explicit; hidden assumptions are where reviewers
   attack.
3. **Specify the relationships.** Name the form of each link: causal, recursive,
   moderating, mediating, constitutive. "X relates to Y" is not a relationship — specify
   direction, shape, and why.
4. **Articulate the mechanism.** The *why*. The mechanism is the engine that makes the
   relationship hold. A proposition without a mechanism is a guess. (Develop the mechanism
   logic with `amr-data-analysis`.)
5. **Write the propositions.** Each proposition is a falsifiable theoretical claim that
   follows from the constructs + mechanism. Number them (P1, P2...). Each must be preceded
   by the argument that earns it.
6. **Set boundary conditions.** State when the theory holds and when it does not — the
   contextual, temporal, and level limits. Boundary conditions are a contribution, not a
   disclaimer.

## Construct definition template

For each construct, fill:

- **Label** (one term, used consistently throughout)
- **Conceptual definition** (one or two precise sentences)
- **Domain** — included instances / excluded instances
- **Distinction** — how it differs from the nearest existing construct
- **Level of theory** (individual / dyad / group / organization / field)

## Proposition discipline

- A proposition states a *relationship between constructs*, not an empirical magnitude.
- Every proposition is preceded by its logical argument; the proposition is the *summary* of an argument already made.
- Propositions build on each other; later ones may depend on earlier constructs.
- Keep them theoretical (P: "the stronger A, the more likely B, because mechanism M"), never operational ("A measured by survey predicts B at p<.05").

## Checklist

- [ ] Every construct has a definition, a domain, and a distinction from neighbors
- [ ] All assumptions are stated explicitly
- [ ] Each relationship's form is specified (causal / recursive / moderating / mediating / constitutive)
- [ ] Each proposition has an explicit mechanism behind it
- [ ] Propositions are numbered and each is earned by a preceding argument
- [ ] Boundary conditions specify where the theory holds and fails
- [ ] Level(s) of theory are consistent (or level shifts are theorized, not accidental)

## Anti-patterns

- Propositions stated as bullet points with no preceding logical argument
- A new construct that is an old construct with a new name
- "X affects Y" with no specified form and no mechanism
- Assumptions left implicit, then exposed by reviewers
- A "process model" figure standing in for the theoretical argument it should summarize
- Boundary conditions written as apologies ("limited to...") rather than as theory
- Smuggling in empirical claims ("data show...") — AMR has no data

## Output format

```
【Constructs】[name: definition / domain / distinction / level] for each
【Assumptions】[explicit list]
【Relationships】[construct → construct : form + mechanism]
【Propositions】P1...Pn (each with one-line mechanism)
【Boundary conditions】where the theory holds / fails
【Next step】amr-methods (refine construction) → amr-data-analysis (logic check)
```
