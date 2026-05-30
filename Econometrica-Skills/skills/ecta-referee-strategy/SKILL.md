---
name: ecta-referee-strategy
description: Use to red-team an Econometrica manuscript before submission and to anticipate co-editor and referee objections — proof gaps, generality, missing finite-sample evidence, and competing methods. Predicts and pre-empts attacks; it does not draft the response letter after reports arrive (use ecta-rebuttal).
---

# Referee and Co-Editor Strategy (ecta-referee-strategy)

## When to trigger

- Before submitting, to find the hole a referee will find first
- When you suspect a proof step or a generality claim is the weak point
- When choosing how to present the contribution to survive a demanding referee pool
- When deciding what to put in the body vs. the Online Appendix to pre-empt objections

Econometrica's referees are usually experts in exactly your method — often the authors of
the results you build on. Reviews are demanding, multi-round, and the **co-editor and
referees check proofs closely**. Assume every step will be read by someone who could have
proven it themselves.

## How Econometrica review works (durable norms)

- A co-editor handles the paper and weighs referee reports; the co-editor's read carries
  decisive weight.
- Referees verify proofs, not just plausibility. A single genuine gap can sink the paper.
- Review times are long and there are typically **multiple rounds** of demanding revision.
- A "revise and resubmit" is a real opportunity but signals substantial remaining work.

(Verify any current procedural specifics on the journal site; the norms above are durable.)

## Red-team the paper

Attack your own manuscript in the order a referee will:

1. **Is the contribution real and general?** Could a referee say "this is a special case of
   [known theorem]" or "this only works for the example"? Pre-empt with an explicit
   nesting/generality statement (see `ecta-topic-selection`, `ecta-literature-positioning`).
2. **Is every proof complete?** Hunt for "easy to see," unstated regularity conditions, a CLT
   or fixed-point theorem whose hypotheses you have not verified, a uniqueness claim with no
   argument. This is the most common rejection cause (see `ecta-theory-model`).
3. **Are the assumptions minimal and defensible?** A referee will ask why each is needed and
   whether a weaker one suffices. Have the answer ready (or weaken the assumption now).
4. **Is there finite-sample evidence?** Asymptotics with no Monte Carlo invites rejection. Are
   the designs fair, the competitors real, the size controlled (see `ecta-robustness`)?
5. **Did you ignore the obvious competitor?** A referee will name the method you should have
   compared to. Compare to it.
6. **Does the replication package actually reproduce?** A non-reproducing package is a credibility
   problem the Data Editor will surface (see `ecta-replication-package`).

## Presentation choices that help

- Put the **hard step of the proof in full** where a referee can find it; do not hide it.
- A short **"Discussion of Assumptions"** subsection naming what each buys and what relaxing it
  would cost defuses the "why this assumption?" line of attack.
- An **Online Appendix** with extra results, robustness, and the long proofs lets the body stay
  clean while pre-empting "what about X?"
- Acknowledge limitations explicitly; a referee who finds an unstated limitation distrusts the rest.

## Suggested vs. excluded referees

- Suggest referees who know the method and have no conflict (no recent coauthorship, advisor /
  advisee, same department). Suggesting people who cannot fairly evaluate the work helps no one.
- If there is a genuine reason to exclude someone (active dispute, direct competitor on the same
  result), note it factually.

## Checklist

- [ ] Generality / nesting pre-empted with an explicit statement
- [ ] Every proof step complete; no unstated regularity condition or unverified theorem hypothesis
- [ ] Each assumption justified; weaker alternatives considered
- [ ] Finite-sample evidence present, fair, and against a real competitor
- [ ] Obvious competing method addressed
- [ ] Replication package reproduces from a clean checkout
- [ ] Limitations stated honestly
- [ ] Referee suggestions are qualified and conflict-free

## Anti-patterns

- Submitting with a known soft spot in a proof, hoping the referee misses it (they will not)
- Burying the hard step so the referee must reconstruct it — and gets annoyed
- No comparison to the method everyone in the field would reach for
- Suggesting only friendly or unqualified referees
- Treating the co-editor's likely concerns as an afterthought
- Assuming one round of revision; planning as if acceptance is near when an R&R is the realistic best case

## Output format

```
【Most likely rejection cause】proof gap / thin generality / no finite-sample / ignored competitor / ...
【Proof audit】complete / gaps at: [...]
【Generality defense】...
【Finite-sample defense】...
【Competitor addressed】yes/no
【Pre-empt moves】[discussion-of-assumptions, online appendix item, ...]
【Referee suggestions】[qualified, conflict-free]
【Next step】ecta-submission
```
