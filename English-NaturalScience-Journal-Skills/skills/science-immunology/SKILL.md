---
name: science-immunology
description: Use when targeting Science Immunology (Sci Immunol) or deciding whether an immunology manuscript fits this AAAS specialist venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science Immunology (science-immunology)

## Journal positioning

Science Immunology is the AAAS specialist immunology journal in the Science family, launched to publish mechanistic immunology research of the highest significance with a particular emphasis on broad relevance and translational potential. Compared to Nature Immunology and Immunity (Cell Press), Science Immunology explicitly values the interface between basic immune mechanisms and human disease — it prizes studies that illuminate fundamental immune biology while having a clear line of sight to human health, including infection, autoimmunity, allergy, cancer immunology, and vaccination. The journal's AAAS editorial culture means a paper must be written for an audience slightly broader than pure immunologists: the advance must be legible and compelling to a scientifically literate non-immunologist. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAAS Science Immunology site.

## When to trigger

- The author names Science Immunology as the target for a mechanistic immunology study with translational or human relevance.
- An immunology paper with strong human data or clinical relevance is being placed among Science Immunology, Nature Immunology, Immunity, and Journal of Experimental Medicine.
- The author wants to understand where Science Immunology sits relative to Nature Immunology (broader relevance / human focus valued) and Immunity (Cell Press, deep mechanism).
- The author needs Science Immunology's desk-reject criteria and a credible alternative-venue list.

## Scope & topic fit

- Mechanisms of human immune responses: studies that combine mouse model mechanistic data with human immunological validation — patient cohorts, human cell systems, or clinical observations — are particularly valued.
- Vaccines and protective immunity: basic mechanisms of vaccine-induced immunity, correlates of protection, adjuvant mechanisms, and germinal-center dynamics with translational relevance.
- Infection immunology: mechanistic dissection of innate and adaptive responses to viral, bacterial, and parasitic pathogens, especially where human immune data complement in vivo mouse findings.
- Autoimmunity and inflammatory disease mechanisms: molecular and cellular pathways underlying human autoimmune diseases (lupus, RA, IBD, MS) studied with mechanistic rigor and human immunological evidence.
- Cancer immunology: mechanisms of anti-tumor immunity, immune-checkpoint regulation, and tumor microenvironment — with emphasis on relevance to human cancer immunotherapy.
- Developmental immunology and immune aging: thymic selection, peripheral homeostasis, and age-related changes in immune function, especially with human data.

## Method & evidence bar

- Human immunological data are a distinguishing strength: patient cohorts, healthy-donor immune profiling, clinical trial immune monitoring, or ex vivo human-cell experiments should complement (not replace) in vivo mouse mechanistic work.
- In vivo mouse genetic experiments remain essential for mechanistic claims; purely observational human studies without mechanistic in vivo corroboration rarely clear the bar.
- Single-cell genomics and systems immunology approaches should be paired with targeted mechanistic experiments that validate key findings at the protein and functional level.
- Translational alignment: even basic-mechanistic papers should articulate why the mechanism matters for a human immune condition; this alignment is explicit in the Introduction and Discussion, not an afterthought.
- Reproducibility and data availability: raw sequencing data in GEO/SRA; flow cytometry data in appropriate repositories; analysis code publicly available.
- AAAS reporting standards: a structured or unstructured abstract per AAAS format; ARRIVE-equivalent or equivalent animal welfare statements; ethics/IRB declarations for human data.

## Structure & house style

- Research Articles are the primary format; the AAAS Science family uses a compact front-matter (summary paragraph) followed by the main text — re-check current article-type conventions on the live site.
- A summary paragraph (different from a structured abstract) may be required; this paragraph must convey the advance to a non-immunologist in plain language.
- The introduction frames both the basic immunological gap and its disease or human-health relevance; the two motivations are presented together, not sequentially.
- Figures should be self-contained; a model figure summarizing the proposed mechanism is expected for mechanistic papers.
- Supplementary Materials carry additional experiments, gating strategies, statistical details, and dataset documentation; Science Immunology expects these to be comprehensive.
- Data and code availability statements, along with materials availability and accession numbers, are required.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Science Immunology author instructions" and follow the current AAAS version.
- Re-check article-type definitions, word and figure limits, and the current summary-paragraph or abstract format requirements.
- Re-check AAAS data and code availability requirements; confirm sequencing data deposition (GEO/SRA) and flow cytometry repository expectations.
- Re-check ethics/IRB declarations for human samples and clinical data; ARRIVE or equivalent reporting for animal experiments; biosafety declarations for pathogen work.
- Confirm competing-interests and funding disclosures, AI-use policy, and preprint compatibility with AAAS policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the immune mechanism established and why it matters for human immunity, disease, or health — not just for mouse immunology.
- [ ] Human immunological data complement the in vivo mouse mechanistic findings; the paper does not rely on mouse data alone for conclusions claimed to be translationally relevant.
- [ ] The summary paragraph or abstract conveys the advance to a general Science family reader, not only to immunologists.
- [ ] Mechanistic in vivo genetic data, with appropriate controls and multiple alleles, underpin the core claims.
- [ ] Sequencing and flow cytometry data are deposited; code is publicly available with documentation.
- [ ] The paper is positioned against recent Science Immunology, Nature Immunology, and Immunity literature on the same immune process.

## Common desk-reject triggers

- A mouse-only mechanistic immunology paper without any human data, translational framing, or obvious line of sight to a human immune condition — this is more appropriate for Nature Immunology or Immunity.
- A purely descriptive human immune profiling or biomarker study without mechanistic in vivo grounding.
- A clinical trial immunomonitoring study where the immune mechanism is secondary to trial results — better suited to clinical journals.
- A study of an immune phenomenon whose scope is so specialized that significance is not legible to a broader Science family readership.
- Methodological immunology papers without a discovery of immune biology — better suited to Nature Methods or a technology-focused venue.

## Re-routing decision

- Deep mechanistic mouse immunology without human component: `nature-immunology` or `immunity` (Cell Press).
- Rigorous in vivo immunology below Science Immunology's significance bar: `journal-of-experimental-medicine` (Rockefeller UP, in vivo rigor, mechanistic immunology/disease).
- Host-pathogen immunology where the microbe mechanism drives the story: `nature-microbiology` or `cell-host-and-microbe`.
- Translational immunology at the mechanism-to-bedside interface: `science-translational-medicine` or `nature-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science Immunology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the study combine in vivo mechanistic data with human immunological relevance at the Science Immunology bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / summary-paragraph format / GEO-SRA deposition / ARRIVE / IRB / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
