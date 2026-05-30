# Cell Skills

<p align="center">
  <img src="assets/cover.png" alt="Cell (Cell Press) cover card" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Cell%20(Cell%20Press)-006699)](https://www.cell.com/cell/home)
[![Scope](https://img.shields.io/badge/scope-molecular%20%26%20cell%20biology-1f6feb)](https://www.cell.com/cell/home)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Cell** (Cell Press) — the flagship molecular and cell-biology research journal.

This pack is opinionated. It is **not** a generic "scientific writing" toolbox. It is a **Cell-specific** stack that encodes the journal's editorial bar — **a complete, mechanistic, hypothesis-driven story** with multiple converging lines of evidence — and the concrete conventions that follow: the single-narrative Article, the signature **Highlights / eTOC blurb / Graphical Abstract** trio, the ≤150-word unstructured **Summary**, **STAR Methods** with the **Key Resources Table** and **Resource Availability**, data/code deposition (with **Mendeley Data** as Elsevier's default), Cell Press **author–date** references, and a conceptual-advance cover letter.

---

## Why a Separate Cell Skill Stack?

Cell imposes constraints that differ materially from field journals — and from Nature/Science:

| Constraint                | Cell                                                          | Implication                                                  |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| Editorial bar             | A **complete, mechanistic story** with converging evidence   | Single-observation / descriptive papers are **pre-review rejected** |
| Article structure         | Summary · Intro · Results · Discussion · **STAR Methods**     | A free-text Methods section is off-style                     |
| Signature artifacts       | **Highlights**, **eTOC blurb**, **Graphical Abstract**       | Missing/weak artifacts hurt at every editorial stage         |
| Highlights                | 3–4 bullets, each **≤ 85 characters**                        | Full sentences or overruns are non-compliant                 |
| Summary (abstract)        | Single paragraph, **≤ ~150 words**, mechanism named, quantified | Long/structured abstracts are off-style                   |
| Methods                   | **STAR Methods** + Key Resources Table + Resource Availability | Reagents need source + RRID/catalog #                     |
| Data & code               | Deposited with accession/DOI; **Mendeley Data** default; 3-bullet statement | "On request" not acceptable for primary data       |
| References                | **Author–date**, **alphabetical** list, full author lists     | Numbered-by-appearance (Science) must be converted          |
| Over-claiming             | A top rejection reason; reviewers demand a complete story    | Conclusions must not outrun the evidence                    |

Generic "scientific writing" packs do not encode these venue constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install cell-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Cell-Skills

mkdir -p ~/.claude/skills && cp -R skills/cell-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cell-* ~/.codex/skills/
```

### First Prompt

```
Use cell-workflow to tell me which skill I should use next for my manuscript targeted at Cell.
```

---

## Default Workflow

```text
cell-fit            (clear the complete-mechanistic-story bar first)
        ▼
cell-framing        (lock the single narrative arc: hypothesis → mechanism → significance)
        ▼
cell-writing        (Article structure; hold length; STAR Methods, not free-text)
        ▼
cell-figures        (display items within budget)
        ▼
cell-star-methods   (Key Resources Table + Resource Availability + QSA)
        ▼
cell-data           (data / code deposition + 3-bullet availability statement)
        ▼
cell-summary        (≤150-word Summary — polish)
        ▼
cell-highlights     (Highlights + eTOC blurb + Graphical Abstract — polish)
        ▼
cell-citation       (Cell Press author–date style — polish)
        ▼
cell-submission     (cover letter + preflight)
        ▼
cell-rebuttal       (after review)
```

`cell-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `cell-workflow`      | Router — decides which sub-skill to invoke next                          |
| `cell-fit`           | Pre-review filter: complete mechanistic story; Cell Press venue routing  |
| `cell-framing`       | Lock the single narrative arc and a declarative title                    |
| `cell-highlights`    | Highlights (≤85 chars), eTOC blurb (~50 words), Graphical Abstract        |
| `cell-summary`       | ≤150-word unstructured Summary, mechanism named, quantified              |
| `cell-writing`       | Article structure; length budget (~45,000 chars); STAR Methods location  |
| `cell-figures`       | Column sizing (85/114/174 mm), ≥6–7 pt fonts, show-the-data, integrity    |
| `cell-star-methods`  | Key Resources Table + Resource Availability (3 subsections) + QSA         |
| `cell-data`          | Deposition (GEO/PDB/PRIDE/Mendeley Data), accessions, 3-bullet statement  |
| `cell-citation`      | Cell Press author–date style, alphabetical list, full author lists        |
| `cell-submission`    | Full preflight checklist + cover-letter template                          |
| `cell-rebuttal`      | Decision triage, experiment prioritization, point-by-point response       |

### Resources

- [`skills/cell-submission/templates/checklist.md`](skills/cell-submission/templates/checklist.md) — full preflight checklist
- [`skills/cell-submission/templates/cover_letter_template.md`](skills/cell-submission/templates/cover_letter_template.md) — conceptual-advance cover-letter scaffold
- [`resources/external_tools.md`](resources/external_tools.md) — deposition repositories, STAR Methods/RRID standards, figure/stats tooling, and key Cell Press author pages

---

## Differences vs. Nature / Science / Cell Press siblings

| Dimension          | Cell                              | Nature / Science                   | Molecular Cell / Cell Reports / CRM |
|--------------------|-----------------------------------|------------------------------------|-------------------------------------|
| Bar                | Complete mechanistic story        | Top-1% broad significance          | Cell Reports: more accepting        |
| Signature artifact | Highlights + eTOC + Graphical Abstract | One-sentence summary (Science) / summary paragraph (Nature) | Same Cell Press artifacts |
| Abstract           | **Summary**, ≤150 w, unstructured | Science ≤125 w + one-sentence summary | Similar Cell Press Summary       |
| Methods            | **STAR Methods** + KRT            | Methods section / Supplementary    | Also STAR Methods                   |
| References         | **Author–date, alphabetical**     | Science: **numbered by appearance** | Cell Press author–date              |
| When to switch     | —                                 | If you want the widest audience    | Molecular Cell (molecular focus) / Cell Reports (less broad) / CRM (translational) |

> Note: Cell uses **author–date** references — the **opposite** of *Science*'s numbered-by-appearance style. For Science, see the sibling [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) pack; for Nature, see [nature-skills](https://github.com/Yuan1z0825/nature-skills).

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## Disclaimer

This is an independent, community-built skill pack. It is **not** affiliated with, endorsed by, or produced by Cell Press, Elsevier, or *Cell*. All targets (word counts, character limits, item limits, style rules) reflect publicly documented author guidelines at the time of writing — **always confirm against the current [Cell author guidelines](https://www.cell.com/cell/authors) and [STAR Methods guidelines](https://www.cell.com/star-methods)** before submitting.

---

## License

MIT
