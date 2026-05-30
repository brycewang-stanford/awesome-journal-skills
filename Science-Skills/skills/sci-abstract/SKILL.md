---
name: sci-abstract
description: Use to write the Science one-sentence summary and the ≤125-word abstract — both readable by a general scientific audience, both leading with the advance. Late-stage polish skill.
---

# Abstract & One-Sentence Summary (sci-abstract)

## When to trigger

- Significance, framing, and format are settled (do this late).
- The abstract reads like a method recap with no result.
- There is no one-sentence summary, or it restates the title.
- The abstract exceeds ~125 words or is dense with jargon/acronyms.

## Two distinct artifacts Science requires

### 1. One-sentence summary (≤ ~125 characters)

A single declarative sentence for the table of contents and editors. It is **not** the title and **not** the first line of the abstract.

- States the finding and its general point.
- No undefined acronyms; readable by any scientist.
- Active voice. Example shape: "A single mutation rewires metabolism, explaining cold tolerance across insects."

### 2. Abstract (≈ 100–125 words, unstructured prose)

Science abstracts are short, single-paragraph, **no subheadings**. Target the educated general scientist, not the subfield.

Recommended five-move structure (no labels in the text):

1. **Context / stakes** (1 sentence) — the broad problem.
2. **Gap / question** (1 sentence) — what was unknown.
3. **What we did** (1 sentence) — approach, in plain terms.
4. **Key result, quantified** (1–2 sentences) — the advance, with numbers.
5. **Implication** (1 sentence) — why a broad community should care.

## Hard constraints

- [ ] ≤ ~125 words (check the current author guidelines for the exact cap; treat 125 as the ceiling).
- [ ] No subheadings, no citations, no figure/table references in the abstract.
- [ ] Define any acronym on first use, or avoid it.
- [ ] At least one **quantified** result — not "significantly increased" but "increased 2.4-fold (P < 0.001)".
- [ ] First sentence is comprehensible to a scientist outside the field.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,"
- Strings of ≥2 undefined acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "leverage" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".

## Quantification check

Every claim of effect must carry a number somewhere in the paper, and the headline effect should be in the abstract: magnitude + unit + uncertainty (CI or P). If the abstract has zero numbers, it is not finished.

## Output format

```
【One-sentence summary】 "..." (char count: N ≤ 125)
【Abstract】 single paragraph (word count: N ≤ 125)
【Five moves present?】 context / gap / approach / quantified result / implication
【Quantified headline result?】 yes/no + the number
【Jargon hits removed】 [...]
【Next】 sci-citation
```

## Anti-patterns

- **Do not** make the one-sentence summary a paraphrase of the title.
- **Do not** open the abstract with method or organism; open with the stake.
- **Do not** end on "further work is needed" — end on the implication.
- **Do not** pad to sound comprehensive; the cap is a feature.
