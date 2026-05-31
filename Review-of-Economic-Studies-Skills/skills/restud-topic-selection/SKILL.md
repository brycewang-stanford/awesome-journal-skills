---
name: restud-topic-selection
description: Use when evaluating whether a research idea clears the REStud top-5 bar, or when sharpening a fuzzy idea into one clean original contribution for a The Review of Economic Studies (REStud) manuscript. Diagnoses fit and contribution; does not draft prose or design empirics.
---

# REStud Topic Selection (restud-topic-selection)

## When to trigger

- A new project just started and the contribution cannot be compressed into one sentence
- The user is unsure whether the idea is REStud-level or a field-journal paper
- A prior desk rejection needs diagnosing — was the *topic* the problem?
- The paper "feels solid" but no senior colleague has agreed it is top-5

## The REStud bar

REStud is general-interest and field-agnostic: founded in **1933 to advance theoretical *and* applied economics, especially by younger economists**, it weights theory and applied work equally — a distinct profile from the more empirically tilted top-5s. What it consistently rewards is a **clean, original contribution presented rigorously and economically**. The contribution must be one of:

1. **A new model** — a tractable framework that delivers an economic insight others did not have
2. **A new identification strategy** — a credible research design that makes a previously hard causal question answerable
3. **A striking new empirical fact** — a robust, surprising regularity that reshapes how a literature thinks

A paper clears the bar when **all** of the following hold:

- **Originality.** The core object — model, design, or fact — is genuinely new, not a competent re-run of a known toolkit on new data.
- **Technical excellence.** Theory: correct, complete proofs. Empirics: state-of-the-art design and inference.
- **Elegance / economy.** The contribution is legible quickly; the result does not require the reader to wade through the appendix to see why it matters.
- **General interest.** A reader outside the immediate subfield can see why the result is interesting.

If the core object is merely an incremental extension, the realistic target is a strong field journal, not REStud.

## The contribution-sentence test

Force the contribution into one sentence:

```
We show that [result], which is new because [prior work could not / believed otherwise],
established via [a new model / a new identification strategy / a new empirical fact],
and this matters for [the broader economic question Q].
```

Failure diagnoses:

- **Result vague** → the question is not yet a question
- **"new because" blank** → this is an extension; reconsider venue
- **Mechanism of novelty is "more data"** → field-journal signal, not REStud
- **Q absent** → no general interest; subfield journal

## Novelty audit

1. Has someone in NBER / CEPR / SSRN already posted this? Search before writing.
2. What is the single closest paper, and what does yours add — new model, new design, new fact, opposite sign?
3. Could a referee compress your contribution into "we already knew that"?
4. Could a referee compress it into "true but not interesting / not economics"?
5. Is the contribution *one* thing, stated cleanly — or a bundle of three half-results?

A "yes" to (3) or (4), or a bundle in (5), is fatal at REStud.

## Junior-scholar note

REStud is well known for being friendly to young scholars — the annual **REStud Tour / "May Meetings"** showcases job-market-stage work by junior economists. If this is a job-market paper, the originality and elegance bar is exactly the same; the practical implication is that a single, sharp, well-executed contribution is more valuable than a sprawling paper. Verify current Tour eligibility and timing on the journal's official page.

## Checklist

- [ ] Contribution compresses to one sentence with the novelty clause filled
- [ ] Core object is clearly one of {new model, new design, new fact}
- [ ] Closest published paper named and the marginal contribution stated
- [ ] Result has general interest beyond the immediate subfield
- [ ] Not a bundle — the paper makes one clean point
- [ ] At least one senior reader agrees it is plausibly top-5

## Anti-patterns

- Choosing REStud for prestige rather than fit; a field-journal acceptance beats two top-5 rejections
- A contribution sentence containing "and we also explore ..." — the *and* is where the paper dies
- "Incremental contribution dressed as novelty" — REStud referees punish this fast
- Weak or generic motivation ("X is important and understudied") with no sharp question
- Treating heavy technical machinery as the contribution when the economic payoff is thin

## Output format

```
【CONTRIBUTION SENTENCE】<one line, novelty clause filled>
【CORE OBJECT】new model | new identification | new empirical fact
【CLOSEST PAPER】<cite> — marginal contribution: <one line>
【GENERAL INTEREST】yes / no — to whom outside the subfield
【KILL SWITCHES TRIGGERED】<list or "none">
【NEXT SKILL】restud-literature-positioning
```
