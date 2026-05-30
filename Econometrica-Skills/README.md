# Econometrica Skills

<p align="center">
  <img src="assets/cover.svg" alt="Econometrica journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Econometrica-1b2a4a)](https://www.econometricsociety.org/publications/econometrica)
[![Index](https://img.shields.io/badge/index-Econometric%20Society-c9a227)](https://www.econometricsociety.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Econometrica** — the journal of the Econometric Society and the field's flagship for **econometric theory, microeconomic theory, game theory, decision theory**, and rigorous structural / empirical work.

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is an **Econometrica-specific** stack built around mathematical rigor: a new method or theorem with a **complete, correct proof**, prized for generality and elegance, supported by identification and asymptotic theory (or axioms and existence/uniqueness), finite-sample (Monte Carlo) evidence, a terse formal house style, and a replication package under the journal's Data and Code Availability Policy.

> Volatile specifics — the current editorial board, the exact submission fee, the member discount, the impact factor, and the precise wording of the Data and Code Availability Policy — change over time. This stack encodes durable norms and tells you to verify current figures on the [official journal page](https://www.econometricsociety.org/publications/econometrica).

---

## Why a Separate Econometrica Skill Stack?

Econometrica imposes constraints that differ materially from general-interest applied journals (AER / QJE / JPE) and from applied-field journals:

| Constraint | Econometrica | Implication |
|------------|--------------|-------------|
| Discipline | Econometric theory, micro / game / decision theory, rigorous structural / empirical | A pure off-the-shelf application is off-fit, however well executed |
| Contribution | A new method or theorem | "Policy evaluation with a known estimator" reads as the wrong venue |
| Proofs | **Complete and correct**; referees check them line by line | A single genuine gap can sink the paper |
| Generality | Prized over narrow application | "Works only for this example" is a rejection signal |
| Structure | Definitions → assumptions → theorems → proofs | Long full proofs live in the Online / Supplementary Appendix |
| Finite-sample evidence | Required for methods papers | Asymptotics with no Monte Carlo invites rejection |
| Regularity conditions | Stated, primitive, minimal | Hidden / high-level conditions are flagged |
| Replication | Strict Data and Code Availability Policy, verified | Monte Carlo tables must reproduce bit-for-bit |
| Process | Editorial Express; long, multi-round review | Plan for major revision, not quick acceptance |
| House style | Terse, formal, theorem-numbered | Narrative applied-paper prose reads as off-register |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/econometrica-skills
/plugin install econometrica-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/econometrica-skills.git
cd econometrica-skills

mkdir -p ~/.claude/skills && cp -R skills/ecta-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ecta-* ~/.codex/skills/
```

### First Prompt

```
Use ecta-workflow to tell me which skill I should use next for my Econometrica manuscript.
```

---

## Default Workflow

```text
ecta-topic-selection
        ▼
ecta-literature-positioning
        ▼
ecta-identification
        ▼
ecta-theory-model
        ▼
ecta-robustness
        ▼
ecta-tables-figures
        ▼
ecta-writing-style        (polish)
        ▼
ecta-replication-package
        ▼
ecta-referee-strategy
        ▼
ecta-submission
        ▼
ecta-rebuttal
```

`ecta-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `ecta-workflow` | Router — decides which sub-skill to invoke next |
| `ecta-topic-selection` | Generality / depth fit + theorem-style contribution statement |
| `ecta-literature-positioning` | Precise formal placement against the methods / theory lineage |
| `ecta-identification` | Identification conditions & asymptotic theory; or axioms & existence/uniqueness |
| `ecta-theory-model` | Central theorem(s), assumptions, generality, and proof strategy |
| `ecta-robustness` | Monte Carlo design, finite-sample performance, regularity / edge cases |
| `ecta-tables-figures` | Self-contained simulation tables and empirical / illustrative exhibits |
| `ecta-writing-style` | Terse formal house style; numbered assumptions and theorems |
| `ecta-replication-package` | Code (+ data) under the Data and Code Availability Policy |
| `ecta-referee-strategy` | Red-team proofs, generality, and finite-sample evidence; co-editor read |
| `ecta-submission` | Editorial Express preflight + Online Appendix assembly + checklist/template |
| `ecta-rebuttal` | Response-letter structure and revision discipline for a (major) R&R |

### Resources

- [`skills/ecta-submission/templates/manuscript_template.md`](skills/ecta-submission/templates/manuscript_template.md) — Theory/methods manuscript skeleton (assumptions, theorems, proof sketches, Online Appendix)
- [`skills/ecta-submission/templates/checklist.md`](skills/ecta-submission/templates/checklist.md) — 11-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Typesetting (LaTeX / `amsthm`), symbolic / computation (Mathematica / SymPy / Julia / MATLAB), and reproducibility toolchain

---

## Differences vs. General-Interest Applied Econ Skills

| Dimension | Econometrica | General-interest applied (AER / QJE / JPE) |
|-----------|--------------|---------------------------------------------|
| Core product | A method or theorem | An answer to an economic question |
| Proofs | Complete, refereed line by line | Often light; method off the shelf |
| Generality | Prized; "only this example" rejected | A clean identified effect can carry the paper |
| Finite-sample evidence | Required for methods papers | Robustness of an estimate, not of an estimator |
| House style | Terse, formal, theorem-numbered | More narrative / motivational |

If the contribution is the *answer to an economic question* with an off-the-shelf method, a general-interest applied pack is the better fit.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Quarterly-Journal-of-Economics-Skills](https://github.com/brycewang-stanford/awesome-journal-skills) — QJE
- [Journal-of-Political-Economy-Skills](https://github.com/brycewang-stanford/awesome-journal-skills) — JPE

---

## License

MIT
