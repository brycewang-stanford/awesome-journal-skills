# PNAS Skills

<p align="center">
  <img src="assets/cover.png" alt="PNAS cover card" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PNAS-005a9c)](https://www.pnas.org/)
[![Scope](https://img.shields.io/badge/scope-multidisciplinary-1f6feb)](https://www.pnas.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **PNAS** (Proceedings of the National Academy of Sciences) — the broad-coverage multidisciplinary journal of the U.S. National Academy of Sciences.

This pack is opinionated. It is **not** a generic "scientific writing" toolbox. It is a **PNAS-specific** stack that encodes the journal's editorial bar — **high quality and broad significance, more accepting than Science/Nature** — and the concrete conventions that follow: the unique **submission tracks** (Direct vs Contributed by an NAS member), the mandatory **≤120-word Significance Statement**, the **Biological/Physical/Social Sciences classification** system, the **~250-word self-contained abstract**, **in-text Materials and Methods**, PNAS **numbered references** in order of appearance, statistics and reproducibility reporting, and mandatory data/code availability.

---

## Why a Separate PNAS Stack?

PNAS imposes constraints that differ materially from field journals — and from Science/Nature:

| Constraint                | PNAS                                                          | Implication                                                  |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| Editorial bar             | High quality + broad significance; **more accepting** than Science/Nature | Values solid important science, not only the flashiest result |
| Submission track          | **Direct** (editor-assigned) vs **Contributed** (NAS member, ≈2/yr, arranges ≥2 reviewers) | The track shapes handling and reviewer choice — pick it early |
| Significance Statement    | Mandatory, **≤120 words**, for a non-specialist               | Missing/weak or just-the-abstract-again hurts at triage      |
| Abstract                  | **~250 words**, single self-contained paragraph, quantified   | Do **not** use a Science ≤125-word abstract or one-sentence summary |
| Classification            | One division (**Biological / Physical / Social**) + minor subject + keywords | Required at submission                                       |
| Methods location          | **Materials and Methods kept in the main text**               | Unlike Science Reports / Cell, do not strip Methods out      |
| References                | Numbered, in order of appearance, full author lists           | Author–date must be converted                               |
| Data & code               | Data Availability Statement + deposition with accession/DOI; "on request" not acceptable | No accession numbers = not submission-ready                 |

Generic "scientific writing" packs do not encode these venue constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install pnas-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/PNAS-Skills

mkdir -p ~/.claude/skills && cp -R skills/pnas-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/pnas-* ~/.codex/skills/
```

### First Prompt

```
Use pnas-workflow to tell me which skill I should use next for my manuscript targeted at PNAS.
```

---

## Default Workflow

```text
pnas-fit            (clear the broad-significance bar; confirm PNAS is the venue)
        ▼
pnas-track          (Direct vs Contributed — decide early)
        ▼
pnas-writing        (structure, classification + keywords, Methods in-text)
        ▼
pnas-figures        (display items within budget)
        ▼
pnas-statistics     (rigor + reproducibility)
        ▼
pnas-data           (data / code availability + deposition)
        ▼
pnas-significance   (≤120-word Significance Statement — high-value)
        ▼
pnas-abstract       (~250-word self-contained abstract — polish)
        ▼
pnas-citation       (PNAS numbered style — polish)
        ▼
pnas-submission     (preflight + cover letter)
        ▼
pnas-rebuttal       (after review)
```

`pnas-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill               | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `pnas-workflow`     | Router — decides which sub-skill to invoke next                          |
| `pnas-fit`          | Broad-significance bar; PNAS vs Science/Nature vs field journal           |
| `pnas-track`        | **Direct vs Contributed (NAS member)** submission track — unique to PNAS  |
| `pnas-significance` | The mandatory **≤120-word Significance Statement** for a broad audience   |
| `pnas-abstract`     | **~250-word** self-contained abstract; distinct from the significance statement |
| `pnas-writing`      | Structure, length, **classification + keywords**, **Methods in-text**     |
| `pnas-figures`      | Column sizing (9/11.4/18 cm), fonts, show-the-data, colorblind-safe        |
| `pnas-statistics`   | Effect size + CI + n + test; replication; randomization; reproducibility   |
| `pnas-data`         | Data Availability Statement, repository deposition, accession/DOI, code    |
| `pnas-citation`     | PNAS numbered style, order of appearance, full author lists                |
| `pnas-submission`   | Full preflight checklist + cover-letter template                          |
| `pnas-rebuttal`     | Decision triage, experiment prioritization, point-by-point response        |

### Resources

- [`skills/pnas-submission/templates/checklist.md`](skills/pnas-submission/templates/checklist.md) — full preflight checklist
- [`skills/pnas-submission/templates/cover_letter_template.md`](skills/pnas-submission/templates/cover_letter_template.md) — PNAS cover-letter scaffold (significance + track + suggested editor/reviewers)
- [`resources/external_tools.md`](resources/external_tools.md) — deposition repositories, reporting standards, figure/stats tooling, and key PNAS author pages

---

## Differences vs. Science / Nature

| Dimension          | PNAS                                  | Science                          | Nature                            |
|--------------------|---------------------------------------|----------------------------------|-----------------------------------|
| Bar                | High quality + broad significance; **more accepting** | Top-1% broad significance        | Top-1% broad significance         |
| Submission track   | **Direct vs Contributed (NAS member)** | Single route                     | Single route                      |
| Plain-language artifact | **Significance Statement ≤120 words** | One-sentence summary             | Summary paragraph                 |
| Abstract           | **~250 words**, self-contained         | ≤ ~125 words                     | Summary-paragraph convention      |
| Methods            | **In the main text** (Materials and Methods) | Supplementary (Reports)          | Methods section conventions       |
| References         | Numbered, order of appearance, full author lists | Numbered, order of appearance    | Different numbered convention     |

For Science, see the sibling [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) pack. For Nature, see [nature-skills](https://github.com/Yuan1z0825/nature-skills).

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## Disclaimer

This is an independent, community-built skill pack. It is **not** affiliated with, endorsed by, or produced by the National Academy of Sciences (NAS) or *PNAS*. All targets (word counts, item limits, track quotas, style rules) reflect publicly documented author guidelines at the time of writing — **always confirm against the current [PNAS Information for Authors](https://www.pnas.org/author-center/submitting-your-manuscript)** before submitting.

---

## License

MIT
