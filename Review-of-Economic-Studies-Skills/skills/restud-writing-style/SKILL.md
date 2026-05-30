---
name: restud-writing-style
description: Use when polishing the prose of a The Review of Economic Studies (REStud) manuscript — introduction, abstract, and overall economy of exposition — so the original contribution reads clearly and elegantly. Polishes writing; does not change results, design, or model.
---

# REStud Writing Style (restud-writing-style)

## When to trigger

- The introduction runs long and buries the contribution
- The abstract reads as motivation rather than result
- Prose is wordy; the reader cannot find the one clean point quickly
- The paper is technically done but reads as a working paper, not a REStud article
- A seminar comment was "I couldn't tell what the contribution was"

## REStud house style

REStud prizes a contribution "presented rigorously **and economically**." The writing standard follows:

- **Clarity over flourish.** Plain, precise English. The reader should never reread a sentence to parse it.
- **Economy.** Say it once, well. Cut sentences that restate. The elegance the journal rewards is partly a property of the prose.
- **Result-forward.** The reader learns what the paper finds early — in the abstract, and again in the first page — not after five pages of motivation.
- **References: author-date** (Harvard style), e.g., "(Card and Krueger, 1994)" and "Card and Krueger (1994) show ...". Verify the current style guide on the journal's official page before final formatting.

## The introduction

A REStud introduction is not the AER five-paragraph formula by decree, but the same logic serves it well:

1. **The hook and the question** — the broad economic question, stated so a non-specialist cares.
2. **What we do** — the contribution: the new model, design, or fact, in one or two sentences.
3. **How** — the method/design and the key idea that makes it work ("why now / why not before").
4. **What we find** — the headline result, with magnitude.
5. **Why it matters / related work** — the contribution located against the closest papers (hand off to `restud-literature-positioning` if this is thin).

Keep it tight. The editor and referees form a judgment in the first two pages.

## The abstract

- One short paragraph. State the question, the contribution (model/design/fact), the headline finding, and why it matters — in that order.
- **Result, not motivation.** "We document/show/prove X" — not "X is an important and understudied question."
- Verify the current word limit on the journal's official author guidelines before submission.

## Prose discipline

- Active voice for what *you* did ("we show", "we estimate"); reserve passive for processes.
- One idea per paragraph; topic sentence first.
- Define each term once; do not toggle synonyms for the same object.
- Cut hedging stacks ("it may perhaps possibly suggest"); state the claim and its caveat once.
- Equations are part of the sentence — punctuate them and gloss every symbol in words on first use.

## Checklist

- [ ] Contribution stated by the end of page 1
- [ ] Abstract leads with result, not motivation, and is within the current limit
- [ ] Introduction has hook / what / how / find / matters, tightly
- [ ] No paragraph restates a prior paragraph
- [ ] Author-date references used consistently
- [ ] Every symbol glossed in words on first use
- [ ] A non-specialist could state the contribution after two pages

## Anti-patterns

- An introduction that spends 3+ pages on motivation before naming the contribution
- An abstract that sells importance instead of stating the result
- Wordiness and redundancy that obscure an otherwise clean point
- Numbered/footnoted reference style when the journal uses author-date
- Synonym-toggling for the same variable, forcing the reader to re-map notation
- Treating writing polish as a step *before* the result and design are stable

## Output format

```
【CONTRIBUTION ON PAGE 1?】yes / no
【ABSTRACT】result-forward / motivation-heavy — word count vs current limit
【INTRO STRUCTURE】hook / what / how / find / matters — present?
【REFERENCE STYLE】author-date confirmed
【REDUNDANCY CUT】<lines/paragraphs removed>
【NEXT SKILL】restud-replication-package | restud-submission
```
