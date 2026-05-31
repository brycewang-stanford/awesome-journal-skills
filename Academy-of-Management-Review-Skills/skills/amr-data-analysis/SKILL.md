---
name: amr-data-analysis
description: Use when stress-testing the LOGIC of an Academy of Management Review (AMR) theory manuscript — checking logical coherence, running thought experiments and counterfactuals, addressing alternative explanations and disconfirming cases, and verifying each proposition follows from its argument. This is ARGUMENT DEVELOPMENT, NOT data analysis; AMR publishes no datasets, no statistics, and no empirical results.
---

# Argument Development & Logic Check (amr-data-analysis)

> **AMR publishes NO empirical data.** There is nothing to estimate, plot, or test. The
> "analysis" in an AMR paper is the *analysis of the argument itself*: does each
> proposition follow logically from the constructs and mechanisms? At AMR, logical
> soundness plays the role that statistical rigor plays at empirical journals.

## The empirical-analog reframe (keep the folder, change the content)

This skill replaces an empirical "identification + robustness" stage. The mapping:

| Empirical sibling (AMJ/ASQ/SMJ) | AMR theory analog |
|---------------------------------|-------------------|
| Identification strategy (IV, DiD, RD, matching) | Generative **mechanism** — the *why* (Whetten 1989, DOI 10.5465/amr.1989.4308371) |
| Robustness checks / alternative specifications | **Internal consistency** + counterfactual probes on premises |
| Ruling out confounders | Engaging and bettering the strongest **rival theory** |
| Replication package (data + code) | **Transparent reasoning** — premises and derivations a reader can re-derive |
| "Estimates are significant and robust" | **Propositions are falsifiable in principle** (AMR's "testable knowledge-based claims") |

There is no instrument, no parallel-trends test, no placebo here; their presence signals a
misfiled empirical paper.

## When to trigger

- Propositions are written but you are not sure they actually follow from the argument
- The theory "feels right" but has not been adversarially tested
- A reviewer would raise an alternative explanation you have not addressed
- The argument chain has hidden leaps between premises

## The four logic tests

Run every proposition through these before drafting.

### 1. Premise-to-conclusion check (per proposition)

For each Pn, write the chain explicitly: premise → premise → mechanism → conclusion. If
any step is missing, the proposition is asserted, not derived. Use a Toulmin frame:
claim / grounds / warrant / backing / rebuttal. The *warrant* (the mechanism that licenses
the inference) is where most theory papers are thin.

### 2. Thought experiment / counterfactual

Manipulate the focal construct in your head and trace the consequence: "If construct X
rose sharply while everything else held, what does the theory predict for Y, and is that
prediction sensible?" Then run the counterfactual: "Under what condition would X move and
Y *not* follow?" If the counterfactual is plausible and unexplained, you are missing a
boundary condition (route back to `amr-theory-development`).

### 3. Alternative-explanation audit

For each proposition, name the strongest *rival* theoretical account of the same
relationship. Then either (a) show why your mechanism is more complete/parsimonious, or
(b) integrate the rival as a boundary condition. Ignoring rivals is the fastest path to a
reject — reviewers *are* the rival theorists.

### 4. Disconfirming-case search

Actively look for a case where the proposition should fail. A theory that "explains
everything" explains nothing. Either the disconfirming case is covered by a stated
boundary condition, or the proposition needs to be narrowed.

## Internal-coherence checks across the whole theory

- **Consistency**: no two propositions contradict each other (unless the tension is the point and is theorized). Constructs mean the same thing throughout — no concept drift (a core Suddaby construct-clarity criterion, AMR 2010, DOI 10.5465/amr.2010.0419).
- **Non-circularity**: a construct is not defined by its effects, then used to explain those effects.
- **Sufficiency**: the constructs and mechanisms are enough to generate the propositions — nothing is smuggled in mid-argument.
- **Parsimony**: every construct earns its place; drop any that does no logical work.

Exemplar: Oliver (AMR 1991, DOI 10.5465/amr.1991.4279002) "analyzes" by argument — deriving
a typology and propositions from antecedent conditions and addressing why organizations might
resist rather than conform (the rival expectation) — all logic, no data.

## Checklist

- [ ] Each proposition has an explicit premise → mechanism → conclusion chain
- [ ] The warrant (mechanism) for each inference is stated, not assumed
- [ ] A thought experiment has been run on each focal relationship
- [ ] Counterfactuals are addressed by boundary conditions, not ignored
- [ ] The strongest alternative explanation for each proposition is named and handled
- [ ] A disconfirming case has been sought for each proposition
- [ ] The theory is internally consistent, non-circular, sufficient, and parsimonious
- [ ] No empirical evidence is invoked as proof (AMR has none)

## Anti-patterns

- Propositions presented as self-evident, with the argument left to the reader
- Hand-waving the mechanism ("it stands to reason that...")
- Defending the theory by asserting it would be "supported by data" — there are no data
- Ignoring the obvious rival theory the reviewers hold
- A theory that cannot be wrong: no boundary, no disconfirming case, no rebuttal addressed
- Circular reasoning: defining a construct by the outcome it is meant to explain

## Output format

```
【Per-proposition logic】P1: chain ok? / gap at warrant? ... Pn
【Thought experiments run】[focal construct → predicted consequence]
【Counterfactuals → boundary conditions】[...]
【Alternative explanations handled】[rival → resolution]
【Disconfirming cases】[case → covered by boundary / narrow proposition]
【Coherence】consistent / non-circular / sufficient / parsimonious : pass/fix
【Next step】amr-contribution-framing
```
