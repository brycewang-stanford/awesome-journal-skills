---
name: pnas-workflow
description: Use when deciding which pnas-* sub-skill to invoke next, or when sequencing a manuscript from significance test through reviewer rebuttal for PNAS (Proceedings of the National Academy of Sciences). Routes — it does not replace — the specialized skills.
---

# PNAS Workflow Router (pnas-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which pnas-* skill to use at the current stage** of a manuscript aimed at *PNAS* (Proceedings of the National Academy of Sciences).

PNAS publishes across three broad divisions — **Biological Sciences, Physical Sciences, and Social Sciences** — and every research article is filed under one of them plus a minor subject area (`pnas-writing`). Two things make PNAS unlike Science or Nature and reshape the workflow: the **submission track** decision (Direct vs Contributed by an NAS member — `pnas-track`) and the mandatory **Significance Statement** (`pnas-significance`). Settle the track early; it changes how the paper is handled and reviewed.

## When to trigger

- "What should I do next with this draft?"
- A draft arrives and you must diagnose the current bottleneck.
- The user is unsure whether to use Direct or Contributed submission.
- Reviews arrive from PNAS and you need to switch into rebuttal mode.

## The single most important gate

PNAS is selective but **more accepting than Science or Nature**: it values solid, important science, not only the flashiest top-1% result. The first question is still **"is this broadly significant and high-quality enough for a general scientific readership?"** — but a strong, rigorous, important paper that is *not* the splashiest discovery of the year still has a real home here. Route to `pnas-fit` first, always; it also handles the realistic step-down from Science/Nature.

## Routing table

| Current symptom                                              | Next skill          |
|-------------------------------------------------------------|---------------------|
| Not sure the result is broad/significant enough, or stepping down from Science/Nature | `pnas-fit`     |
| Unsure whether to use Direct or Contributed (NAS-member) submission | `pnas-track`  |
| No Significance Statement, or it just restates the abstract  | `pnas-significance` |
| Abstract too long/narrow; conflated with significance statement | `pnas-abstract` |
| Structure unclear; Methods misplaced; no classification/keywords | `pnas-writing` |
| Figures over budget; sizing/fonts/colors non-compliant       | `pnas-figures`      |
| Stats under-reported; n/error bars/tests unclear; not reproducible | `pnas-statistics` |
| No data/code availability plan or deposition                 | `pnas-data`         |
| References not in PNAS numbered style                        | `pnas-citation`     |
| About to submit; need a preflight checklist + cover letter   | `pnas-submission`   |
| Received reviews / a revision decision                       | `pnas-rebuttal`     |

## Default order

1. `pnas-fit` — clear the broad-significance bar; confirm PNAS is the right venue
2. `pnas-track` — pick Direct vs Contributed (do this early; it shapes handling)
3. `pnas-writing` — structure, length, classification + keywords, Methods placement
4. `pnas-figures` — finalize display items within budget
5. `pnas-statistics` — rigor & reproducibility reporting
6. `pnas-data` — data / code availability + deposition
7. `pnas-significance` — the ≤120-word Significance Statement (high-value)
8. `pnas-abstract` — ≤250-word self-contained abstract (late polish)
9. `pnas-citation` — PNAS numbered reference style (late polish)
10. `pnas-submission` — preflight + cover letter
11. `pnas-rebuttal` — after review

> `pnas-significance`, `pnas-abstract`, and `pnas-citation` are **late-stage polish** — but the Significance Statement is high-value and editor-facing, so do not leave it to the last minute. Draft it as soon as the claim is locked.

## Decision shortcuts

- "Is this PNAS-level, or should it go to a field journal / up to Science?" → `pnas-fit`
- "A co-author is an NAS member and offered to communicate the paper" → `pnas-track`
- "I have an abstract but no Significance Statement" → `pnas-significance`
- "My significance statement is just the abstract again" → `pnas-significance`
- "Where do Materials and Methods go?" → `pnas-writing` (PNAS keeps them **in the main text**)
- "What classification do I file under?" → `pnas-writing`
- "No accession numbers / no code repo" → `pnas-data`

## How PNAS differs from Science and Nature

- **More accepting**: PNAS publishes solid, important, broadly significant work across Biological/Physical/Social Sciences — a sound realistic target when a paper is strong but not the single splashiest result Science/Nature chase. `pnas-fit` makes the step-down call.
- **Submission tracks**: PNAS uniquely offers **Direct Submission** (standard, editor-assigned, peer reviewed) and **Contributed Submission** (an NAS member communicates their own paper and arranges reviewers, limited to a few per member per year). The older Prearranged Editor option and the discontinued "Communicated" track are covered in `pnas-track`. No Science/Nature equivalent.
- **Significance Statement**: PNAS requires a separate **≤120-word Significance Statement** written for a broad scientific reader — not Science's one-sentence summary, not Nature's summary paragraph. See `pnas-significance`.
- **Abstract**: PNAS abstracts run to **~250 words** — do **not** copy Science's ≤125-word abstract or one-sentence summary.
- **Methods**: PNAS keeps a **Materials and Methods** section in the main text (unlike Science Reports / Cell, which push methods elsewhere).

## Anti-patterns

- **Do not** skip `pnas-fit` and start polishing prose.
- **Do not** decide the track at the end — it shapes editor handling and reviewer choice (`pnas-track`).
- **Do not** treat the Significance Statement as a formality bolted on at submission.
- **Do not** generate a rebuttal before the main text is actually revised.
