# Awesome Journal Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

A curated index of **journal-specific agent skill packs** for social-science manuscript work — selecting topics, identifying causal effects, writing introductions, formatting tables, preparing replication packages, and responding to reviewers.

Each pack is **journal-specific by design**: it encodes the editorial preferences, formatting conventions, identification standards, and review culture of a single target venue. Generic "scientific writing" skill packs miss these constraints.

---

## Why "Journal-Specific" Skills?

Top journals impose constraints that differ materially across venues:

- **AER** desk-rejects on identification design (TWFE, weak IV, naive RDD).
- **《管理世界》** desk-rejects on missing China institutional context.
- **《经济研究》** desk-rejects on missing canonical theory citations.

A one-size-fits-all "economics writing" skill cannot encode these differences. Each pack here is opinionated by venue.

---

## The Skill Packs

| Venue                          | Repository                                                                                  | Discipline                       | Status  |
|--------------------------------|---------------------------------------------------------------------------------------------|---------------------------------|---------|
| **American Economic Review** + AER:Insights + AEJ family | [AER-skills](https://github.com/brycewang-stanford/AER-skills)                              | Economics (top-5)                | v1.0    |
| **《管理世界》** (Management World)        | [management-world-skills](https://github.com/brycewang-stanford/management-world-skills)    | Management + applied economics  | v0.1    |
| **《经济研究》** (Economic Research)        | [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills)  | Economics (China-CSSCI top)     | v0.1    |

---

## Repository Layout

This repo embeds each pack as a **git submodule** pinned to its own upstream repository. A scheduled GitHub Action ([`.github/workflows/sync-submodules.yml`](.github/workflows/sync-submodules.yml)) bumps the pins to the latest upstream `main` daily, so this repo mirrors the source packs without manual intervention.

```text
awesome-journal-skills/
├── AER-skills/                 → submodule of brycewang-stanford/AER-skills
├── economic-research-skills/   → submodule of brycewang-stanford/economic-research-skills
├── management-world-skills/    → submodule of brycewang-stanford/management-world-skills
└── .github/workflows/sync-submodules.yml
```

Clone with submodules populated:

```bash
git clone --recurse-submodules https://github.com/brycewang-stanford/awesome-journal-skills.git
# or, if already cloned:
git submodule update --init --recursive
```

Pull latest pack content locally at any time:

```bash
git submodule update --remote --merge
```

---

## How to Use

### Option A — Claude Code Plugin (recommended)

For each pack you want:

```bash
# AER
/plugin marketplace add https://github.com/brycewang-stanford/AER-skills
/plugin install aer-skills

# 管理世界
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills
/plugin install management-world-skills

# 经济研究
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills

/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/AER-skills.git
git clone https://github.com/brycewang-stanford/management-world-skills.git
git clone https://github.com/brycewang-stanford/economic-research-skills.git

mkdir -p ~/.claude/skills
cp -R AER-skills/skills/aer-* ~/.claude/skills/
cp -R management-world-skills/skills/mw-* ~/.claude/skills/
cp -R economic-research-skills/skills/er-* ~/.claude/skills/
```

### First Prompt

```
Use aer-workflow (or mw-workflow / er-workflow) to tell me which skill I should
use next for my manuscript targeted at <journal>.
```

---

## Pack-Selection Cheat Sheet

| Your manuscript looks like…                            | Use this pack                |
|--------------------------------------------------------|------------------------------|
| Causal-identification empirical paper aimed at top-5 econ | `AER-skills`                |
| China-context empirical paper with policy actionability   | `management-world-skills`   |
| China-context paper with theoretical grounding            | `economic-research-skills`  |

---

## Roadmap

Next-step TODO: build journal-specific packs for the 20 + 20 venues below. Open an issue to upvote a specific venue.

### English — 20 mainstream econ & management journals

1. Quarterly Journal of Economics (QJE) — *econ*
2. Journal of Political Economy (JPE) — *econ*
3. Econometrica — *econ*
4. Review of Economic Studies (REStud) — *econ*
5. Review of Economics and Statistics (REStat) — *econ*
6. Journal of Economic Perspectives (JEP) — *econ*
7. Journal of Econometrics — *econ*
8. AEJ: Applied Economics — *econ*
9. AEJ: Macroeconomics — *econ*
10. Journal of Development Economics (JDE) — *econ*
11. Journal of Finance (JF) — *finance*
12. Journal of Financial Economics (JFE) — *finance*
13. Review of Financial Studies (RFS) — *finance*
14. Academy of Management Journal (AMJ) — *management*
15. Academy of Management Review (AMR) — *management*
16. Administrative Science Quarterly (ASQ) — *management*
17. Strategic Management Journal (SMJ) — *strategy*
18. Management Science — *OM / general management*
19. Journal of Marketing (JM) — *marketing*
20. The Accounting Review (TAR) — *accounting*

### Chinese — 20 mainstream econ & management journals (经管)

1. 《经济学（季刊）》 — *经济学*
2. 《世界经济》 — *经济学*
3. 《中国工业经济》 — *经济学*
4. 《金融研究》 — *金融*
5. 《中国农村经济》 — *经济学*
6. 《数量经济技术经济研究》 — *计量*
7. 《财经研究》 — *经济学*
8. 《财贸经济》 — *经济学*
9. 《经济学动态》 — *经济学*
10. 《国际金融研究》 — *金融*
11. 《经济科学》 — *经济学*
12. 《南开经济研究》 — *经济学*
13. 《管理科学学报》 — *管理*
14. 《南开管理评论》 — *管理*
15. 《中国管理科学》 — *管理*
16. 《管理评论》 — *管理*
17. 《管理学报》 — *管理*
18. 《系统工程理论与实践》 — *管理*
19. 《科研管理》 — *管理*
20. 《会计研究》 — *会计*

---

## Contributing

Each pack lives in its own repository. To contribute to a pack, open a PR on that pack's repo. To propose a new pack, open an issue here.

Quality bar for inclusion in this index:

1. Opinionated by venue (not generic)
2. Bilingual zh-CN / en README (for China-relevant venues)
3. At least one `*-workflow` router skill
4. Plugin manifests (`.claude-plugin/plugin.json` + `marketplace.json`)
5. MIT-licensed

---

## Related Projects

Generic scientific-writing skill packs (different scope from this index):

- [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)
- [nature-skills](https://github.com/Yuan1z0825/nature-skills)

---

## License

MIT
