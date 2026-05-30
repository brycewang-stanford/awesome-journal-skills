# JACS Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of the American Chemical Society cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JACS-0a3d62)](https://pubs.acs.org/journal/jacsat)
[![Index](https://img.shields.io/badge/publisher-ACS-e58e26)](https://pubs.acs.org/journal/jacsat)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of the American Chemical Society (JACS)** — a premier, broad-scope chemistry journal published by the American Chemical Society (ACS), spanning organic, inorganic, organometallic, catalysis, materials, physical, analytical, and biological chemistry.

This repository is opinionated. It is **not** a generic "scientific writing" toolbox. It is a **JACS-specific** stack covering scope/venue fit, framing the chemical advance, synthesis and full characterization rigor (NMR / HRMS / IR/UV-vis / elemental analysis or HPLC / single-crystal X-ray with CCDC deposition / catalysis controls and mechanism), ACS-style schemes and figures, the Supporting Information, ACS house style, Article-vs-Communication sizing, the cover letter, Paragon Plus submission, referee strategy, and revision.

> This pack describes **durable norms**, not volatile specifics. Always verify current editors, article types, word/figure limits, fees, and policies on the official ACS author page for JACS.

---

## Why a Separate JACS Skill Stack?

JACS imposes constraints that differ materially from physics letters, math journals, or clinical journals:

| Constraint | JACS | Implication |
|------------|------|-------------|
| Discipline | Broad chemistry (organic / inorganic / catalysis / materials / physical / bio) | Subfield-only advances may fit a specialized ACS journal better |
| Bar | Significant chemical advance of **broad interest** | "More work" ≠ significance; breadth must be argued |
| Evidence | Claims **fully supported** by characterization + controls | Asserted novelty/mechanism gets desk-rejected or torn apart |
| New compounds | Full characterization + demonstrated **purity** | Missing EA/HPLC or clean ¹³C is a rigor red flag |
| Crystal structures | Deposited with the **CCDC**; checkCIF-clean | Undeposited structures block acceptance |
| Mechanism | Supported by controls / kinetics / labeling | A drawn cycle with no probes is "speculative" |
| Supporting Information | Complete procedures, full data, spectra copies, CIFs | "Data on request" is unacceptable |
| Formats | **Article** and **Communication** | Choosing the wrong format invites a misfit critique |
| Submission | **ACS Paragon Plus**; TOC graphic required | Format/file rules are mechanical gates |
| Style | ACS numbered citations; bold compound numbers | Non-ACS formatting reads as careless |

Generic "scientific writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jacs-skills
/plugin install jacs-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jacs-skills.git
cd jacs-skills

mkdir -p ~/.claude/skills && cp -R skills/jacs-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jacs-* ~/.codex/skills/
```

### First Prompt

```
Use jacs-workflow to tell me which skill I should use next for my JACS manuscript.
```

---

## Default Workflow

```text
jacs-scope-fit
        ▼
jacs-results-framing
        ▼
jacs-methods
        ▼
jacs-figures
        ▼
jacs-supplementary
        ▼
jacs-writing-style       (polish)
        ▼
jacs-length-management   (polish)
        ▼
jacs-cover-letter
        ▼
jacs-submission
        ▼
jacs-referee-strategy
        ▼
jacs-revision
```

`jacs-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `jacs-workflow` | Router — decides which sub-skill to invoke next |
| `jacs-scope-fit` | Broad-interest test + JACS vs specialized-journal venue + Article/Communication |
| `jacs-results-framing` | Pin the chemical advance, its breadth driver, and significance |
| `jacs-methods` | Synthesis + full characterization rigor (NMR/HRMS/X-ray/CCDC, catalysis controls/mechanism/kinetics) |
| `jacs-figures` | ACS-style schemes, spectra, ORTEP structures, mechanism figures, TOC graphic |
| `jacs-supplementary` | Supporting Information: procedures, full data, spectra copies, CIFs/CCDC |
| `jacs-writing-style` | ACS house style, nomenclature, units, and claim discipline |
| `jacs-length-management` | Article vs Communication; trim to ACS format norms |
| `jacs-cover-letter` | Editor-facing advance + fit statement |
| `jacs-submission` | ACS Paragon Plus pre-submission preflight + manuscript template |
| `jacs-referee-strategy` | Reviewer suggestions/exclusions + pre-empting standard objections |
| `jacs-revision` | Triage referee reports + point-by-point response |

### Resources

- [`skills/jacs-submission/templates/manuscript_template.md`](skills/jacs-submission/templates/manuscript_template.md) — JACS-style manuscript + SI skeleton (Article/Communication)
- [`skills/jacs-submission/templates/checklist.md`](skills/jacs-submission/templates/checklist.md) — 12-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — characterization platforms, CCDC/PDB deposition, ChemDraw/crystallography/computation software, ACS citation styles

---

## Differences vs. Specialized ACS Journal Stacks

| Dimension | JACS | Specialized ACS journal (e.g., *Org. Lett.* / *Inorg. Chem.* / *ACS Catal.* / *Chem. Mater.*) |
|-----------|------|-----------------------------------------------------------------------------------------------|
| Scope | Broad interest across chemistry | Within-subfield interest |
| Bar | Significant, general advance | Solid, focused contribution |
| Breadth argument | **Required** | Less central |
| Rigor (characterization, CCDC, controls) | Required at the highest bar | Required, subfield-appropriate |
| Format | Article / Communication | Varies by journal |

If your advance is narrow in scope, `jacs-scope-fit` will say so and point you to a better-fit ACS journal.

---

## What This Repo Does Not Do

- It does not write a submission-ready manuscript for you.
- It does not simulate referee preferences or guarantee acceptance.
- It does not store JACS acceptance rates, impact factor, or other volatile metadata.
- It does not judge whether your chemical advance is truly original — that is your scientific judgment.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》 reference pack
- [ACS author resources for JACS](https://pubs.acs.org/journal/jacsat) — official guidelines (verify current rules here)

---

## License

MIT
