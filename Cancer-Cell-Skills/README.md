# Cancer Cell Skills

<p align="center">
  <img src="assets/cover.svg" alt="Cancer Cell (Cell Press) journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Cancer%20Cell-c0392b)](https://www.cell.com/cancer-cell/home)
[![Index](https://img.shields.io/badge/publisher-Cell%20Press-1f6feb)](https://www.cell.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Cancer Cell (Cell Press)** — a leading journal for molecular and translational oncology, covering tumor biology, cancer genetics and genomics, the tumor microenvironment, immuno-oncology, and clinical-translational cancer research.

This repository is opinionated. It is **not** a generic "biomedical writing" toolbox. It is a **Cancer Cell-specific** stack built around the journal's defining demand: a **clear molecular mechanism** validated across **orthogonal systems** (cultured cells, in vivo models, and ideally human / patient data), reported with **STAR Methods** rigor, and framed for **translational relevance** without overclaiming.

> Durable norms only. This pack deliberately avoids volatile specifics (named editors, exact word/figure caps, fees, impact factor). Always verify current requirements on the official Cell Press / Cancer Cell author pages and the live STAR Methods guidelines before submitting.

---

## Why a Separate Cancer Cell Skill Stack?

Cancer Cell imposes constraints that differ materially from broad-scope journals and from clinical-trial journals like JAMA:

| Constraint                  | Cancer Cell                                                       | Implication                                                      |
|-----------------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| Discipline                  | Molecular / translational oncology (not clinical-trial reporting) | Pure descriptive omics or a single cell-line story is off-fit    |
| Core demand                 | Mechanism **plus** translational relevance                        | "Interesting correlation" without mechanism reads as incremental |
| Validation                  | Orthogonal systems: cells + in vivo + human tumor data            | Conclusions from one system are routinely rejected               |
| Rigor                       | STAR Methods + Key Resources Table mandatory                      | Unauthenticated cell lines / undefined `n` are desk-level flags  |
| Reproducibility             | Cell-line authentication, mycoplasma testing, antibody validation | Missing these is a reviewer-punished gap                          |
| Animal work                 | IACUC approval + ARRIVE-style reporting, randomization, blinding  | "n mice" with no power/allocation detail invites rejection       |
| Statistics                  | `n` defined as biological replicates; correct tests; error bars   | Pseudo-replication and undefined error bars are common rejections |
| Data / code                 | Deposition: GEO / SRA (sequencing), PRIDE (MS), PDB (structures)  | "Data available on request" is not acceptable                    |
| Format                      | Cell Press structure: Summary, Highlights, eTOC, graphical abstract | Not an IMRaD clinical template                                  |
| Claims                      | Therapeutic claims require in vivo and/or human validation        | Overstated translational claims are a signature reviewer target  |

Generic "scientific writing" packs do not encode these Cell Press and Cancer Cell specifics.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cancer-cell-skills
/plugin install cancer-cell-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/cancer-cell-skills.git
cd cancer-cell-skills

mkdir -p ~/.claude/skills && cp -R skills/cc-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cc-* ~/.codex/skills/
```

### First Prompt

```
Use cc-workflow to tell me which skill I should use next for my Cancer Cell manuscript.
```

---

## Default Workflow

```text
cc-scope-fit
        ▼
cc-study-design
        ▼
cc-reporting-standards
        ▼
cc-statistics
        ▼
cc-figures-tables
        ▼
cc-structured-abstract
        ▼
cc-ethics-registration
        ▼
cc-writing-style      (polish)
        ▼
cc-cover-letter
        ▼
cc-submission
        ▼
cc-peer-review-revision
```

`cc-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                          |
|-----------------------------|----------------------------------------------------------------------------------|
| `cc-workflow`               | Router — decides which sub-skill to invoke next                                  |
| `cc-scope-fit`              | Is this a Cancer Cell paper? Mechanism + translational-relevance gate            |
| `cc-study-design`           | Experimental design across cells / mouse / PDX / organoid / human tumor systems  |
| `cc-reporting-standards`    | STAR Methods, Key Resources Table, cell-line / antibody / animal rigor           |
| `cc-statistics`             | Biological statistics: defining `n`, replicates, tests, multiple comparisons     |
| `cc-figures-tables`         | Multi-panel mechanistic figures, quantification, image integrity                 |
| `cc-structured-abstract`    | Summary + eTOC blurb + Highlights + graphical abstract                           |
| `cc-ethics-registration`    | IACUC / IRB / consent / biosafety + data-availability and deposition statements  |
| `cc-writing-style`          | Cell Press house style: Summary / Results / Discussion craft, claim calibration  |
| `cc-cover-letter`           | Cover letter framing significance, fit, and suggested / excluded reviewers       |
| `cc-submission`             | Pre-submission preflight + manuscript template (format, files, deposition links) |
| `cc-peer-review-revision`   | Consultative review response: point-by-point, new experiments, claim narrowing   |

### Resources

- [`skills/cc-submission/templates/manuscript_template.md`](skills/cc-submission/templates/manuscript_template.md) — Cell Press manuscript skeleton (Summary, Highlights, STAR Methods, Key Resources Table, data availability)
- [`skills/cc-submission/templates/checklist.md`](skills/cc-submission/templates/checklist.md) — Pre-submission self-check across scope, rigor, statistics, figures, ethics, and deposition
- [`resources/external_tools.md`](resources/external_tools.md) — Oncology data repositories (GEO / SRA / PRIDE / PDB / cBioPortal / TCGA), reporting frameworks, and bioinformatics / imaging software

---

## Differences vs. JAMA Skills

| Dimension          | Cancer Cell (Cell Press)                | JAMA                                    |
|--------------------|------------------------------------------|------------------------------------------|
| Discipline         | Molecular / translational oncology      | Clinical medicine / trials               |
| Core unit          | Mechanism validated across systems      | Patient-level clinical outcome           |
| Methods reporting  | STAR Methods + Key Resources Table      | CONSORT / STROBE + trial registration    |
| Statistics         | Biological `n`, replicates, no pseudo-rep | Pre-specified analysis, ITT, CIs        |
| Structure          | Summary / Highlights / graphical abstract | Structured clinical abstract (IMRaD)   |
| Data sharing       | GEO / SRA / PRIDE / PDB deposition      | De-identified participant data / IPD     |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Cancer Cell (Cell Press)](https://www.cell.com/cancer-cell/home) — Official journal home
- [Cell Press STAR Methods](https://www.cell.com/star-methods) — Structured, Transparent, Accessible Reporting

---

## License

MIT
