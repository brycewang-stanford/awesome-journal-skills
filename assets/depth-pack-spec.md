# Depth-Pack Authoring Contract (single source of truth)

This file is the **exact** standard for first-party journal **depth packs** in this
repository (e.g. `Economic-Research-Journal-Skills/`). Every pack-builder agent MUST
follow it to the letter so all packs are structurally identical and only their
expert content differs.

Reference pack to imitate for tone/structure (read it first):
`Economic-Research-Journal-Skills/` — its `skills/er-workflow/SKILL.md`,
`skills/er-identification/SKILL.md`, `skills/er-submission/SKILL.md`,
`README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`.

---

## 0. Hard rules (do NOT violate)

1. The pack is a **plain directory** committed into this repo. **Never** run `git init`
   inside it, never create a nested `.git`, never make it a submodule.
2. Create **all** files listed in §2. Nothing missing, nothing extra.
3. Content must be **genuinely journal-specific** — real editors/scope, real
   submission portal, real word/format limits, real house-style quirks, real
   exemplar papers, real anti-patterns. **No generic filler**, no "lorem", no TODOs.
4. Language: for an **English-language journal**, SKILL bodies are in **English**.
   For a **Chinese-language journal**, SKILL bodies are in **Chinese**. In both cases
   `README.md` is English and `README.zh-CN.md` is Simplified Chinese.
5. Exactly **12 skills**, named with the discipline skill-set in §5 and the pack's
   skill prefix. The first skill is always `{prefix}-workflow` (the router).

---

## 1. Per-pack identity (provided to you in the task)

- `DIR`         — directory name, e.g. `Quarterly-Journal-of-Economics-Skills`
- `PREFIX`      — skill prefix, e.g. `qje`
- `PLUGIN`      — plugin name (lowercase-dashed), e.g. `qje-skills`
- `TITLE`       — display title, e.g. `Quarterly Journal of Economics (QJE)`
- `FAMILY`      — discipline family (§5): econ | finance | management | clinical | physical | chinese
- `FACTS`       — the journal fact sheet (scope, editors, portal, limits, style, exemplars, anti-patterns)

---

## 2. File list (exact)

```
DIR/
  .gitignore                         # copy §3 verbatim
  LICENSE                            # copy §4 verbatim
  README.md                          # §6 skeleton, English
  README.zh-CN.md                    # §6 skeleton, Chinese
  .claude-plugin/plugin.json         # §7 skeleton
  .claude-plugin/marketplace.json    # §8 skeleton
  resources/external_tools.md        # discipline data sources + software packages
  skills/{prefix}-workflow/SKILL.md
  skills/{prefix}-<skill2>/SKILL.md
  ... (12 skills total, names from §5)
  skills/{prefix}-submission/templates/checklist.md
  skills/{prefix}-submission/templates/manuscript_template.md
```

## 3. `.gitignore` (verbatim)

```
.DS_Store
*.log
*.tmp
.idea/
.vscode/
__pycache__/
*.pyc
.env
node_modules/
*.smcl
*.dta.bak
```

## 4. `LICENSE` (verbatim)

Standard MIT License, `Copyright (c) 2026 Bryce Wang`. Copy the body of
`Economic-Research-Journal-Skills/LICENSE` exactly.

## 5. Discipline skill-sets (12 skills; replace `{p}` with PREFIX)

**econ** (QJE, JPE, Econometrica, REStud):
`{p}-workflow`, `{p}-topic-selection`, `{p}-literature-positioning`,
`{p}-identification`, `{p}-theory-model`, `{p}-robustness`, `{p}-tables-figures`,
`{p}-writing-style`, `{p}-replication-package`, `{p}-referee-strategy`,
`{p}-submission`, `{p}-rebuttal`

**finance** (JF, JFE, RFS):
`{p}-workflow`, `{p}-topic-selection`, `{p}-literature-positioning`,
`{p}-identification`, `{p}-empirical-design`, `{p}-robustness`, `{p}-tables-figures`,
`{p}-internet-appendix`, `{p}-writing-style`, `{p}-submission`,
`{p}-referee-strategy`, `{p}-rebuttal`

**management** (AMJ, AMR, ASQ, SMJ):
`{p}-workflow`, `{p}-topic-selection`, `{p}-theory-development`,
`{p}-literature-positioning`, `{p}-methods`, `{p}-data-analysis`,
`{p}-contribution-framing`, `{p}-tables-figures`, `{p}-writing-style`,
`{p}-submission`, `{p}-review-process`, `{p}-rebuttal`
(AMR is a **theory-only** journal — adapt `-methods`/`-data-analysis` to
theory-construction and conceptual-argument craft.)

**clinical** (JAMA, Cancer Cell):
`{p}-workflow`, `{p}-scope-fit`, `{p}-study-design`, `{p}-reporting-standards`,
`{p}-statistics`, `{p}-figures-tables`, `{p}-structured-abstract`,
`{p}-ethics-registration`, `{p}-writing-style`, `{p}-cover-letter`,
`{p}-submission`, `{p}-peer-review-revision`
(Cancer Cell is **molecular oncology** — adapt `-study-design` to experimental
design, `-reporting-standards` to rigor/reproducibility & data availability,
`-ethics-registration` to animal/IRB + data-deposition.)

**physical** (PRL, JACS, Annals of Mathematics):
`{p}-workflow`, `{p}-scope-fit`, `{p}-results-framing`, `{p}-methods`,
`{p}-figures`, `{p}-supplementary`, `{p}-writing-style`, `{p}-length-management`,
`{p}-cover-letter`, `{p}-submission`, `{p}-referee-strategy`, `{p}-revision`
(Annals of Mathematics is **pure math** — adapt `-methods`→proof-strategy,
`-figures`→exposition, `-supplementary`→appendix/auxiliary-results.)

**chinese** (中国农村经济, 财经研究, 中国行政管理):
`{p}-workflow`, `{p}-topic-selection`, `{p}-literature-review`,
`{p}-identification`, `{p}-mechanism`, `{p}-heterogeneity`, `{p}-tables-figures`,
`{p}-policy-implication`, `{p}-abstract`, `{p}-style`, `{p}-submission`,
`{p}-rebuttal`
(中国行政管理 is **public administration** — adapt identification/mechanism to PA
methods: mixed quant+qual, policy process, case comparison.)

## 5b. SKILL.md format (every skill)

```markdown
---
name: {prefix}-<slug>
description: Use when <precise trigger condition> for a <TITLE> manuscript. <One sentence on what it does and does NOT do.>
---

# <Human title> ({prefix}-<slug>)

## When to trigger
- bullet symptoms

## <Core section: priority list / branches / decision table specific to this stage & journal>

## Checklist
- [ ] concrete, checkable items

## Anti-patterns
- concrete failure modes reviewers at THIS journal punish

## Output format
​```
【...structured handoff naming the next skill...】
​```
```
- 70–130 lines each. The router (`{prefix}-workflow`) instead contains: overview,
  trigger timing, a routing table (symptom → next skill), the default order, and
  anti-patterns — mirror `er-workflow`.

## 6. README skeleton (both languages)

Mirror `Economic-Research-Journal-Skills/README.md`:
title + centered cover `<img src="assets/cover.svg" ...>` (use `.svg` placeholder;
do **not** invent a binary), 4 shields (License/Journal/Index/Claude Code),
`English | [简体中文](README.zh-CN.md)` switcher, one-paragraph positioning, a
"Why a separate stack?" constraint table (journal-specific), Quick Start (plugin +
manual), Default Workflow ASCII pipeline, a Skills table (all 12), Resources list,
a "Differences vs. …" comparison table, Related links, License. README.zh-CN.md is
the faithful Chinese mirror with `[English](README.md) | 简体中文`.

## 7. `plugin.json` skeleton

```json
{
  "name": "{PLUGIN}",
  "description": "<2–3 sentence journal-specific description of the 12-skill stack>",
  "version": "0.1.0",
  "author": { "name": "Bryce Wang", "email": "brycew6m@stanford.edu" },
  "license": "MIT",
  "homepage": "https://github.com/brycewang-stanford/{PLUGIN}",
  "repository": "https://github.com/brycewang-stanford/{PLUGIN}",
  "keywords": ["...8–12 journal/discipline keywords..."]
}
```

## 8. `marketplace.json` skeleton

```json
{
  "$schema": "https://json.schemastore.org/claude-code-marketplace.json",
  "name": "{PLUGIN}",
  "version": "0.1.0",
  "description": "<one-line>",
  "owner": { "name": "Bryce Wang", "email": "brycew6m@stanford.edu" },
  "metadata": { "pluginRoot": "./" },
  "plugins": [
    {
      "name": "{PLUGIN}",
      "version": "0.1.0",
      "source": "./",
      "description": "Twelve-skill bundle covering the <TITLE> manuscript lifecycle.",
      "author": { "name": "Bryce Wang", "email": "brycew6m@stanford.edu" },
      "license": "MIT",
      "homepage": "https://github.com/brycewang-stanford/{PLUGIN}",
      "repository": "https://github.com/brycewang-stanford/{PLUGIN}",
      "keywords": ["...7 keywords..."],
      "category": "academic",
      "skills": ["skills/{prefix}-workflow", "...all 12 in workflow order..."]
    }
  ]
}
```

Both JSON files MUST be valid JSON (no trailing commas). The `skills` array MUST list
all 12 skill directories in workflow order.

## 9. Self-check before finishing

- `ls skills/` shows exactly 12 dirs, each with `SKILL.md`.
- Both `.claude-plugin/*.json` parse as valid JSON; `skills` array has 12 entries.
- `README.md` Skills table has 12 rows matching the dirs.
- No nested `.git`. No placeholder/TODO text.
- Report: the file tree you created + per-SKILL line counts.
