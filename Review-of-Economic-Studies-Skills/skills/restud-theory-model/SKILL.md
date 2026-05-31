---
name: restud-theory-model
description: Use when building, sharpening, or stress-testing the theoretical model in a The Review of Economic Studies (REStud) manuscript — whether a pure-theory paper or an empirical paper with a model — and when routing proofs to the online appendix. Develops the model and its economic payoff; does not run the empirics.
---

# REStud Theory / Model (restud-theory-model)

## When to trigger

- The paper is pure theory and needs the contribution framed as a clean result
- An empirical paper has a model whose assumptions and proofs are underdeveloped
- A proposition is stated but the proof lives inline and clutters the main text
- A referee will ask "what is the economic content of this result, beyond the algebra?"

## What REStud rewards in theory

REStud has unusually deep theory roots for a top-5 journal — it is where **optimal income-taxation theory** (Mirrlees, "An Exploration in the Theory of Optimum Income Taxation," REStud 38(2), 1971) and the **Ramsey–Cass–Koopmans** growth model (Cass, "Optimum Growth in an Aggregative Model of Capital Accumulation," REStud 32(3), 1965) were first published. It accepts theory across all fields and treats a **new model** as a first-class contribution — and with Joint Managing Editors who are themselves theorists (Antonio Penta in mechanism design, Jakub Steiner in information/behavioral economics), pure theory is a first-class citizen here, not a tolerated minority. The bar is **technical excellence with a legible economic payoff**:

- **Tractability with insight.** The model is as simple as it can be and still deliver the result. Generality for its own sake is not the contribution; the *economic* insight is.
- **A clean main result.** One or two propositions that a reader can state in words. If the headline result needs three lemmas to even state, the framing is wrong.
- **Assumptions that earn their place.** Every assumption is either standard, or defended as the minimal one that delivers the result, or shown to be relaxable.
- **Complete, correct proofs** — in the **online appendix / supplementary file** (REStud's standard home for full proofs), not the main text.

Unlike Econometrica, which can treat heavy formal machinery as the contribution itself, REStud wants the economics to be visible without wading through the apparatus.

## Building the model section

### Step 1 — Result-first framing

Before the setup, state the main result in one sentence of economics ("agents who face X will choose Y, and welfare rises/falls because Z"). The setup then exists to deliver that sentence.

### Step 2 — Minimal setup

Introduce only the objects the result needs. Defer extensions, generalizations, and special cases to later subsections or the appendix. Define notation once, in a table if it is heavy.

### Step 3 — Propositions and their economics

For each proposition: state it formally, then immediately gloss it in words — what economic force drives it, what comparative static it implies, what it rules out. A proposition with no verbal gloss is incomplete by REStud standards.

### Step 4 — Proofs to the online appendix

Keep main-text proofs to a sketch (the key step / the binding constraint). Full, line-by-line proofs go to the **online appendix**, which REStud uses precisely for this. Number appendix results to match the main text (Proof of Proposition 2, etc.).

### Step 5 — Map to empirics (if applicable)

If the model disciplines an empirical section, state which assumptions are testable, which parameters are identified by which moments, and which predictions the data will confront. Hand identification details to `restud-identification`.

## Checklist

- [ ] Main result stated in one sentence of economics before the setup
- [ ] Setup is minimal — no object that the result does not use
- [ ] Each proposition glossed verbally (economic force, comparative static)
- [ ] Assumptions defended as standard / minimal / relaxable
- [ ] Full proofs in the online appendix; main text has sketches only
- [ ] Notation defined once; a notation table if heavy
- [ ] If empirical: model assumptions mapped to testable predictions

## Anti-patterns

- "Theory without a clear economic payoff" — algebra that yields no insight a reader can state
- Burying the headline proposition behind three lemmas before it can even be stated
- Generality for its own sake when a special case carries the entire insight
- Full multi-page proofs inline, crowding out the economics
- Assumptions introduced silently and used to drive the result without defense
- A model in an empirical paper whose assumptions contradict the estimation sample

## Output format

```
【MAIN RESULT (one sentence)】<economic statement>
【PROPOSITIONS】[stated + verbal gloss] x1-2
【KEY ASSUMPTIONS】[standard / minimal / relaxable — for each]
【PROOFS LOCATION】online appendix (sketches in text)
【EMPIRICAL LINK】testable predictions: [...] (or "pure theory")
【NEXT SKILL】restud-robustness (empirical) | restud-tables-figures | restud-writing-style
```
