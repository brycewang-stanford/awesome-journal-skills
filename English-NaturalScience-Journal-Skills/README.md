# English Natural-Science Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="English Natural-Science Journal Skills — 100 flagship natural-science, clinical & physical-science journals" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-Nature%20%C2%B7%20Cell%20%C2%B7%20NEJM%20%C2%B7%20PRL%20%C2%B7%20JACS-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An opinionated agent skill stack for **100 mainstream English-language natural-science, clinical/medical, physical, and formal-science journals** — the general-science triad (Nature, Science, PNAS), the Cell Press and Nature Portfolio families, the APS Physical Review family, the ACS / RSC / Wiley chemistry flagships, the "big four" general medical journals and the major clinical society venues, and the top pure-mathematics journals.

This is the natural-science sibling of [`English-SocialScience-Journal-Skills`](../English-SocialScience-Journal-Skills/) — the "other 100" complementing that bundle's 100 econ / finance / management journals. Like the siblings, it ships **one self-contained fit-and-house-style skill per journal**, plus `en-natsci-journal-workflow` for routing. Each journal skill helps answer: *is my manuscript on-target, how should it be framed, what method and evidence does this venue expect, and what official submission details must be re-checked?*

The flagship venues that also ship as first-party depth packs in the parent repo (Science, Cell, PNAS, NEJM, The Lancet) and the third-party Nature packs are intentionally covered here as quick fit cards too — exactly as `american-economic-review` is covered both in a depth pack and in the social-science breadth bundle.

## Coverage

| Group | Count |
|---|--:|
| General & multidisciplinary science | 7 |
| Cell, molecular & genome biology | 16 |
| Ecology, evolution & plant biology | 5 |
| Immunology, microbiology & experimental medicine | 4 |
| Open-access & genomics biology | 3 |
| Neuroscience & behaviour | 4 |
| Clinical medicine — general | 7 |
| Clinical medicine — specialty | 11 |
| Translational & cancer medicine | 4 |
| Physics | 9 |
| Astronomy & astrophysics | 3 |
| Chemistry | 10 |
| Materials & energy | 5 |
| Earth, environment & climate | 5 |
| Computer science, AI & engineering | 4 |
| Mathematics | 3 |
| **Total** | **100** |

## Quick Start

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install english-natsci-journal-skills
/reload-plugins
```

Manual copy:

```bash
cp -R skills/* ~/.claude/skills/
# or for Codex
cp -R skills/* ~/.codex/skills/
```

## How to Use

Start with `en-natsci-journal-workflow` when the venue is uncertain — it classifies the manuscript by advance type, evidence shape, audience breadth, and submission goal, then routes to the matching per-journal skill. If the target is already known, name the journal directly, for example: "Use `nature-methods` to assess whether this new tool is generalizable enough for Nature Methods."

Every skill returns a fit verdict, method/evidence requirements, desk-reject risks, official-submission checks, and reroute suggestions.

## Skills

### General & multidisciplinary science (7)

| Skill | Journal |
|---|---|
| `nature` | Nature (Nature) |
| `science` | Science (Science) |
| `pnas` | Proceedings of the National Academy of Sciences (PNAS) |
| `nature-communications` | Nature Communications (Nat Commun) |
| `science-advances` | Science Advances (Sci Adv) |
| `national-science-review` | National Science Review (NSR) |
| `the-innovation` | The Innovation (The Innovation) |

### Cell, molecular & genome biology (16)

| Skill | Journal |
|---|---|
| `cell` | Cell (Cell) |
| `molecular-cell` | Molecular Cell (Mol Cell) |
| `cell-stem-cell` | Cell Stem Cell (Cell Stem Cell) |
| `cancer-cell` | Cancer Cell (Cancer Cell) |
| `cell-metabolism` | Cell Metabolism (Cell Metab) |
| `immunity` | Immunity (Immunity) |
| `neuron` | Neuron (Neuron) |
| `developmental-cell` | Developmental Cell (Dev Cell) |
| `current-biology` | Current Biology (Curr Biol) |
| `nature-genetics` | Nature Genetics (Nat Genet) |
| `nature-methods` | Nature Methods (Nat Methods) |
| `nature-biotechnology` | Nature Biotechnology (Nat Biotechnol) |
| `nature-cell-biology` | Nature Cell Biology (Nat Cell Biol) |
| `nature-structural-and-molecular-biology` | Nature Structural & Molecular Biology (NSMB) |
| `the-embo-journal` | The EMBO Journal (EMBO J) |
| `nucleic-acids-research` | Nucleic Acids Research (NAR) |

### Ecology, evolution & plant biology (5)

| Skill | Journal |
|---|---|
| `nature-ecology-and-evolution` | Nature Ecology & Evolution (Nat Ecol Evol) |
| `molecular-biology-and-evolution` | Molecular Biology and Evolution (MBE) |
| `ecology-letters` | Ecology Letters (Ecol Lett) |
| `the-plant-cell` | The Plant Cell (Plant Cell) |
| `nature-microbiology` | Nature Microbiology (Nat Microbiol) |

### Immunology, microbiology & experimental medicine (4)

| Skill | Journal |
|---|---|
| `nature-immunology` | Nature Immunology (Nat Immunol) |
| `science-immunology` | Science Immunology (Sci Immunol) |
| `cell-host-and-microbe` | Cell Host & Microbe (Cell Host Microbe) |
| `journal-of-experimental-medicine` | Journal of Experimental Medicine (JEM) |

### Open-access & genomics biology (3)

| Skill | Journal |
|---|---|
| `elife` | eLife (eLife) |
| `plos-biology` | PLOS Biology (PLOS Biol) |
| `genome-biology` | Genome Biology (Genome Biol) |

### Neuroscience & behaviour (4)

| Skill | Journal |
|---|---|
| `nature-neuroscience` | Nature Neuroscience (Nat Neurosci) |
| `nature-human-behaviour` | Nature Human Behaviour (Nat Hum Behav) |
| `trends-in-cognitive-sciences` | Trends in Cognitive Sciences (TiCS) |
| `molecular-psychiatry` | Molecular Psychiatry (Mol Psychiatry) |

### Clinical medicine — general (7)

| Skill | Journal |
|---|---|
| `nejm` | The New England Journal of Medicine (NEJM) |
| `the-lancet` | The Lancet (Lancet) |
| `jama` | JAMA (JAMA) |
| `the-bmj` | The BMJ (BMJ) |
| `annals-of-internal-medicine` | Annals of Internal Medicine (Ann Intern Med) |
| `nature-medicine` | Nature Medicine (Nat Med) |
| `plos-medicine` | PLOS Medicine (PLOS Med) |

### Clinical medicine — specialty (11)

| Skill | Journal |
|---|---|
| `the-lancet-oncology` | The Lancet Oncology (Lancet Oncol) |
| `journal-of-clinical-oncology` | Journal of Clinical Oncology (JCO) |
| `the-lancet-infectious-diseases` | The Lancet Infectious Diseases (Lancet Infect Dis) |
| `the-lancet-neurology` | The Lancet Neurology (Lancet Neurol) |
| `circulation` | Circulation (Circulation) |
| `journal-of-the-american-college-of-cardiology` | Journal of the American College of Cardiology (JACC) |
| `european-heart-journal` | European Heart Journal (EHJ) |
| `gastroenterology` | Gastroenterology (Gastroenterology) |
| `gut` | Gut (Gut) |
| `blood` | Blood (Blood) |
| `diabetes-care` | Diabetes Care (Diabetes Care) |

### Translational & cancer medicine (4)

| Skill | Journal |
|---|---|
| `journal-of-clinical-investigation` | Journal of Clinical Investigation (JCI) |
| `science-translational-medicine` | Science Translational Medicine (Sci Transl Med) |
| `cancer-discovery` | Cancer Discovery (Cancer Discov) |
| `ca-a-cancer-journal-for-clinicians` | CA: A Cancer Journal for Clinicians (CA Cancer J Clin) |

### Physics (9)

| Skill | Journal |
|---|---|
| `physical-review-letters` | Physical Review Letters (PRL) |
| `reviews-of-modern-physics` | Reviews of Modern Physics (RMP) |
| `physical-review-x` | Physical Review X (PRX) |
| `nature-physics` | Nature Physics (Nat Phys) |
| `nature-photonics` | Nature Photonics (Nat Photonics) |
| `prx-quantum` | PRX Quantum (PRX Quantum) |
| `physical-review-d` | Physical Review D (PRD) |
| `physical-review-b` | Physical Review B (PRB) |
| `reports-on-progress-in-physics` | Reports on Progress in Physics (RoPP) |

### Astronomy & astrophysics (3)

| Skill | Journal |
|---|---|
| `nature-astronomy` | Nature Astronomy (Nat Astron) |
| `the-astrophysical-journal` | The Astrophysical Journal (ApJ) |
| `monthly-notices-of-the-royal-astronomical-society` | Monthly Notices of the Royal Astronomical Society (MNRAS) |

### Chemistry (10)

| Skill | Journal |
|---|---|
| `journal-of-the-american-chemical-society` | Journal of the American Chemical Society (JACS) |
| `angewandte-chemie-international-edition` | Angewandte Chemie International Edition (Angew Chem Int Ed) |
| `nature-chemistry` | Nature Chemistry (Nat Chem) |
| `chemical-reviews` | Chemical Reviews (Chem Rev) |
| `chemical-society-reviews` | Chemical Society Reviews (Chem Soc Rev) |
| `nature-catalysis` | Nature Catalysis (Nat Catal) |
| `accounts-of-chemical-research` | Accounts of Chemical Research (Acc Chem Res) |
| `chem` | Chem (Chem) |
| `acs-nano` | ACS Nano (ACS Nano) |
| `nature-nanotechnology` | Nature Nanotechnology (Nat Nanotechnol) |

### Materials & energy (5)

| Skill | Journal |
|---|---|
| `nature-materials` | Nature Materials (Nat Mater) |
| `advanced-materials` | Advanced Materials (Adv Mater) |
| `nature-energy` | Nature Energy (Nat Energy) |
| `joule` | Joule (Joule) |
| `energy-and-environmental-science` | Energy & Environmental Science (EES) |

### Earth, environment & climate (5)

| Skill | Journal |
|---|---|
| `nature-geoscience` | Nature Geoscience (Nat Geosci) |
| `nature-climate-change` | Nature Climate Change (Nat Clim Chang) |
| `nature-sustainability` | Nature Sustainability (Nat Sustain) |
| `environmental-science-and-technology` | Environmental Science & Technology (ES&T) |
| `one-earth` | One Earth (One Earth) |

### Computer science, AI & engineering (4)

| Skill | Journal |
|---|---|
| `nature-machine-intelligence` | Nature Machine Intelligence (Nat Mach Intell) |
| `science-robotics` | Science Robotics (Sci Robot) |
| `ieee-transactions-on-pattern-analysis-and-machine-intelligence` | IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) |
| `journal-of-machine-learning-research` | Journal of Machine Learning Research (JMLR) |

### Mathematics (3)

| Skill | Journal |
|---|---|
| `annals-of-mathematics` | Annals of Mathematics (Ann. of Math.) |
| `inventiones-mathematicae` | Inventiones Mathematicae (Invent. Math.) |
| `journal-of-the-american-mathematical-society` | Journal of the American Mathematical Society (JAMS) |

### Routing

| Skill | Role |
|---|---|
| `en-natsci-journal-workflow` | English natural-science journal routing workflow (not a journal) |

## Source Discipline

Editorial rules change. The bundled [`resources/source-basis.md`](resources/source-basis.md) records the reference lists and source policy used for this expansion, and the deliberate omission of volatile facts (impact factors, acceptance rates, word/figure limits, APCs). The [`resources/_build-spec.md`](resources/_build-spec.md) is the canonical template and factual-discipline contract, and [`resources/journal-roster.md`](resources/journal-roster.md) is the locked 100-venue roster. Before final submission, always verify the live official author instructions on the publisher's own site or submission system — for clinical work this includes the applicable reporting guideline (CONSORT / PRISMA / STROBE / ARRIVE) and trial registration.
