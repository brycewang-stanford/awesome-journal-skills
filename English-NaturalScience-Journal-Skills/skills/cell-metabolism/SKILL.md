---
name: cell-metabolism
description: Use when targeting Cell Metabolism or deciding whether a metabolism/physiology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cell Metabolism (cell-metabolism)

## Journal positioning

Cell Metabolism is Cell Press's flagship metabolism and physiology journal, publishing mechanistic studies of how organisms sense, process, and adapt to nutrients, energy, and metabolic stress — with emphasis on in vivo physiology and disease relevance. The core territory is metabolic disease (obesity, type 2 diabetes, NAFLD/NASH, cardiovascular-metabolic risk), mitochondrial biology, aging and longevity, and the metabolic underpinning of organ crosstalk. The readership spans metabolic biologists, physiologists, endocrinologists, and disease-oriented researchers; papers must deliver a mechanistic advance with in vivo grounding, not just a cell-culture phenotype.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Cell Metabolism as the target venue.
- A metabolism/physiology study is deciding between Cell Metabolism and Nature Metabolism, Cell, or a society metabolism journal.
- An in vivo metabolic study needs to assess whether its mechanistic depth and disease relevance meet the bar.
- The author needs this venue's desk-reject patterns and re-routing options.

## Scope & topic fit

- Energy homeostasis mechanisms: nutrient sensing (mTOR, AMPK, insulin signaling), fuel switching, and systemic energy balance studied in vivo.
- Adipose biology, hepatic metabolism, skeletal-muscle fuel utilization — when the mechanistic insight is physiologically grounded.
- Mitochondrial function and dysfunction in physiology and disease: electron transport, dynamics, mitophagy, inter-organellar communication.
- Metabolic aging and longevity mechanisms: calorie restriction mimetics, mTOR/IGF-1/NAD pathways, senescence-metabolism interactions.
- Gut-microbiome interactions with host metabolism when the host-side mechanism is the primary advance.
- Immuno-metabolism and cancer metabolism are in scope when the metabolic mechanism — not the immune or cancer phenotype — is the central contribution.

## Method & evidence bar

- In vivo physiology is the default expectation: genetic mouse models (whole-body or tissue-specific knockouts, knock-ins), dietary or pharmacological perturbation with careful phenotyping (indirect calorimetry, glucose and insulin tolerance, clamp studies, metabolic cage data).
- Mechanism must go beyond phenotype: genetic epistasis, metabolite tracing (stable isotope / 13C flux), or biochemical pathway validation is expected.
- Metabolite profiling or metabolomics should be hypothesis-driven and mechanistically interpreted; untargeted discovery alone is insufficient.
- Translation to human tissue (biopsies, organoids, or cohort correlations) is valued but not always mandatory; absence must be justified.
- STAR Methods required; reagent/data deposition (metabolomics to MetaboLights or equivalent, sequencing to GEO, animal model details) per Cell Press policy.
- Rigor reporting: blinding of outcome assessment in animal studies, group sizes with power justification, sex as a biological variable addressed.

## Structure & house style

- STAR Methods is mandatory; key resources table covers antibodies, mouse strains, software, metabolites/reagents.
- Structured abstract with an "in brief" or "highlights" box; the title is declarative and states the physiological mechanism or disease connection.
- Figures should build a coherent physiological narrative: establish the in vivo phenotype, determine the tissue/cell of action, identify the molecular mechanism, confirm with epistasis or rescue.
- Graphical abstract standard for Cell Press; source data for all quantitative figures required.
- Translational framing in the introduction and discussion must be specific: name the disease context, not just "metabolic syndrome."
- Data and code availability statement required; statistical methods including treatment of sex and replication must be explicit.

## Official-submission checklist

- Search "Cell Metabolism author information" on the Cell Press site and follow the current version.
- Re-check article types (Article, Short Article, Resource), length and figure limits, and supplemental policy.
- Confirm STAR Methods and key resources table requirements for the current submission cycle.
- Re-check animal ethics approval, sex-as-biological-variable reporting, and ARRIVE guidelines compliance.
- Verify competing-interests, funding, and AI-use disclosure requirements.
- Re-check data/metabolomics/sequencing deposition requirements and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the physiological mechanism discovered and its relevance to a metabolic disease or aging.
- [ ] The advance is framed as a mechanistic insight, not as "gene X affects body weight."
- [ ] In vivo data are central; if cell culture predominates, the physiological relevance is rigorously established.
- [ ] Sex as a biological variable is explicitly addressed in the experimental design and statistics.
- [ ] STAR Methods, key resources table, and data/code deposition are prepared.
- [ ] Metabolite tracing, genetic epistasis, or equivalent mechanistic evidence supports causal conclusions.

## Common desk-reject triggers

- Entirely cell-based study with no in vivo component and no convincing justification for why in vivo work is impossible.
- Phenotypic description in a knockout mouse without a mechanistic explanation of how the target drives the metabolic phenotype.
- Metabolomics or proteomics survey with no mechanistic follow-through — a correlation list, not an advance.
- Sex as a biological variable ignored in animal studies without justification.
- Clinical or epidemiological study without a mechanistic molecular story — better suited to Diabetes Care, Cell Reports Medicine, or a clinical endocrinology journal.

## Re-routing decision

- Paradigm-shifting metabolic advance with extremely broad significance → `cell` (if the conceptual reach spans beyond metabolism) or `nature` / `science`.
- Strong metabolic mechanism but somewhat narrower scope → `nature-metabolism` (Springer Nature; same tier, slightly broader tolerance for translational-only studies).
- Cancer-metabolic mechanism with cancer biology as the primary frame → `cancer-cell` or `molecular-cell`.
- Solid mechanistic work below the Cell Metabolism significance bar → `elife`, `plos-biology`, or a society journal such as Diabetes or the Journal of Lipid Research.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cell Metabolism
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the in vivo physiology + mechanism clear Cell Metabolism's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / STAR Methods / animal ethics / sex-as-variable / data-code deposition>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
