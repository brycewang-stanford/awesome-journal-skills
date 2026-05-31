---
name: cancer-cell
description: Use when targeting Cancer Cell or deciding whether a cancer-biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cancer Cell (cancer-cell)

## Journal positioning

Cancer Cell is Cell Press's flagship cancer-biology journal, publishing mechanistic studies that illuminate how tumors initiate, progress, resist therapy, or interact with the immune microenvironment — and that carry explicit translational or clinical relevance. The readership spans cancer biologists, oncologists, and physician-scientists, so a paper must deliver both mechanistic depth and a clear statement of why the finding matters for cancer biology or patient care. Descriptive oncology, biomarker discovery without mechanism, or purely clinical trial reporting do not belong here.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Cancer Cell as the target venue.
- A mechanistic cancer study asks whether its translational framing and evidence depth meet the bar.
- A manuscript sits between Cancer Cell and Cancer Discovery, Nature Cancer, or Cell and the author needs to differentiate.
- The author needs Cancer Cell's most common desk-reject patterns and credible re-routing options.

## Scope & topic fit

- Oncogenic signaling, tumor-suppressor pathways, and driver mutations — studied mechanistically, not descriptively.
- Tumor immunology and the immune microenvironment: mechanism of immune evasion, checkpoint biology, cancer-immune co-evolution.
- Therapy resistance mechanisms with direct relevance to clinical strategies: genetic, epigenetic, or cellular plasticity routes.
- Metabolic reprogramming in cancer, including nutrient sensing and the interaction between cancer cells and the tumor microenvironment.
- Cancer stem cells, clonal evolution, intra-tumor heterogeneity — when the mechanistic insight is clear and the translational implication is explicit.
- Liquid biopsy or multi-omic approaches only when they uncover a mechanistic principle, not when primarily diagnostic.

## Method & evidence bar

- Mechanism is mandatory: a phenotype alone — even in a genetically engineered mouse model or patient-derived xenograft — does not meet the bar without a molecular explanation.
- Genetic validation is expected: at least two orthogonal perturbations (knockout/knockin, RNAi/CRISPR, pharmacological) targeting the same node; rescue experiments for causal claims.
- In vivo models must be fit-for-purpose; purely cell-line-based studies face high skepticism unless the mechanistic logic is very strong and the biology inaccessible in vivo.
- Translational anchor is required: patient-derived material, clinical cohort correlation, or direct clinical implication must be stated and supported, not merely mentioned.
- STAR Methods format required; reagents/cell lines/sequences/data deposited per Cell Press community standards.
- Statistical rigor expected: sample sizes, replicates (biological vs. technical), and appropriate tests reported; code/data availability required.

## Structure & house style

- Cell Press format: structured abstract with a "significance" or "in brief" summary; title is declarative and mechanistic, not a question.
- STAR Methods section is mandatory and must be self-contained; key resources table (antibodies, cell lines, organisms, software, reagents) is a Cell Press standard.
- Figures should narrate a coherent mechanistic story across panels; extended data or supplemental figures carry additional validation; the main figure pathway should be readable without the supplement.
- The introduction positions the study against the current mechanistic understanding, not just citing incidence statistics; the final paragraph of the introduction should state the key advance clearly.
- Significance/In Brief box: a brief plain-language paragraph summarizing the biological question, key findings, and translational relevance — re-check the current format and length requirements.
- Data and code availability statement required; image quantification and source data for all graphs expected.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Cancer Cell author information" or "Cancer Cell submission guidelines" on the Cell Press / current-biology.com site and follow the live version.
- Re-check current article types (Article vs. Short Article vs. Brief Communication), length and figure limits, and supplemental-information policy.
- Confirm STAR Methods requirements and key resources table format for this submission cycle.
- Re-check competing-interests declaration, funding, author-contribution statement, and AI-use disclosure requirements.
- Verify data/code/reagent deposition requirements (GEO for sequencing, PDB for structures, cell-line authentication).
- Confirm the journal's preprint policy and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this mechanism matters for cancer biology or cancer therapy broadly — beyond the tumor type studied.
- [ ] The advance is framed as a mechanistic insight, not as "we show for the first time that gene X is mutated/overexpressed in cancer Y."
- [ ] At least two orthogonal genetic/pharmacological perturbations support the core causal claim.
- [ ] Patient-derived material or clinical data is integrated, not merely cited as motivation.
- [ ] STAR Methods, key resources table, and data/code deposition are prepared.
- [ ] The framing positions the paper against the relevant mechanistic canon in this cancer type or pathway.

## Common desk-reject triggers

- Purely descriptive: a gene is mutated/overexpressed/deleted in cancer, with no mechanistic explanation of how or why.
- Mechanism is proposed but evidence is indirect — no rescue, no orthogonal validation, correlation only.
- Translational hook is absent or superficial: the introduction cites patient statistics, but no patient-derived data or clinical correlation appears in the study.
- Study is entirely cell-line-based with no in vivo component and the biology could be addressed in vivo.
- Clinical-trial or purely biomarker-discovery papers with no mechanistic content — better suited to JCO, JAMA Oncology, or Cancer Discovery's clinical track.

## Re-routing decision

- Strong mechanistic story but less explicit translational angle → `cell` (if the advance is truly paradigm-shifting at the molecular level) or `molecular-cell` (if the mechanism is primarily molecular/structural).
- High-impact translational or clinical-trial result with mechanistic context → `cancer-discovery` (AACR flagship, more clinical-translational latitude).
- Mechanistic immunology of cancer → `immunity` or `nature-immunology` if immunology is the primary advance, not the cancer angle.
- Solid mechanistic study below the Cancer Cell significance bar → `cell-reports`, `cancer-research`, or `oncogene`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cancer Cell
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the mechanism + translational anchor clear Cancer Cell's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / STAR Methods / key resources table / data-code deposition / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
