---
name: nature-immunology
description: Use when targeting Nature Immunology (Nat Immunol) or deciding whether an immunology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Immunology (nature-immunology)

## Journal positioning

Nature Immunology is Springer Nature's premier specialist immunology journal, sitting at the top of the discipline alongside Cell Press's Immunity. It publishes discoveries that shift the conceptual framework of immunology — new mechanisms of immune-cell development, activation, regulation, and effector function, as well as findings that redefine how the immune system intersects with infection, cancer, autoimmunity, and tissue homeostasis. The significance bar is explicitly field-shifting, not merely incremental mechanism; a new co-stimulatory molecule, a new cytokine role, or a new cell subset requires a conceptual storyline that changes how immunologists think about a process broadly. The readership is the full international immunology community; papers that are compelling only to subspecialists rarely pass triage. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature Nature Immunology site.

## When to trigger

- The author names Nature Immunology as the target for a mechanistic immunology study.
- An immunology paper with high-significance in vivo mechanistic findings is being placed among Nature Immunology, Immunity, Science Immunology, and Journal of Experimental Medicine.
- The author needs to understand how Nature Immunology differs from its immediate competitors in significance bar and editorial culture before submission.
- The author needs Nature Immunology's desk-reject triggers and a credible alternative-venue list.

## Scope & topic fit

- Innate and adaptive immunity mechanisms: pattern recognition, signaling cascades downstream of PRRs and antigen receptors, transcriptional control of immune-cell identity and effector programs.
- Lymphocyte biology with field-shifting significance: T-cell differentiation, exhaustion, memory, regulatory mechanisms; B-cell activation, germinal center biology, antibody diversification.
- Innate immune-cell biology: macrophage polarization and tissue-resident populations, dendritic-cell subset function, NK-cell biology, innate lymphoid cells — when the advance is conceptually general.
- Immune regulation and tolerance: Treg biology, central and peripheral tolerance mechanisms, checkpoint molecules — studies that reveal a general immune-regulatory principle.
- Tumor immunology and immunotherapy mechanisms: mechanisms of anti-tumor immunity, immune evasion, checkpoint-blockade response and resistance — mechanistic, not primarily clinical.
- Neuroimmunology, tissue immunity, and microbiota-immune interactions when the immunological mechanism is the primary advance.

## Method & evidence bar

- In vivo genetic mouse models (conditional knockouts, knock-ins, lineage tracing) combined with flow cytometry, scRNA-seq, or imaging to resolve cell-type-specific mechanisms are the standard approach; purely in vitro or ex vivo findings without in vivo corroboration rarely suffice.
- Genetic claims require multiple independent alleles or rigorous rescue experiments; Cre-lox specificity must be validated with appropriate controls.
- Single-cell genomics data should be supported by protein-level and functional validation; descriptive scRNA-seq atlases without mechanistic follow-up do not clear the bar.
- Human immune data: patient cohorts must have appropriate clinical phenotyping, and translational claims must have mechanistic grounding in the in vivo animal model.
- Data deposition: raw sequencing data in GEO/SRA; flow cytometry data in appropriate repositories; code for genomic analyses publicly available.
- A Nature Life Sciences Reporting Summary is required; ARRIVE guidelines or equivalent for animal experiments; IRB/ethics for human samples.

## Structure & house style

- Articles are the primary format; Letters exist but check current article-type options on the live site.
- The title should convey a mechanistic discovery, not a cell-type or phenotype: "Mechanism controlling X in Y cells" rather than "Role of gene X in immunity."
- The abstract must make the conceptual advance accessible to all immunologists — specialists in adaptive and innate immunity alike — within its first two sentences.
- Extended Data carries mechanistically essential supporting experiments; Supplementary Information holds detailed flow-cytometry gating strategies, secondary analyses, and large dataset files.
- A single central model figure illustrating the proposed mechanism is expected; it should clearly delineate what is established in this paper versus prior work.
- Methods must include sufficient reagent detail (clone numbers, antibody suppliers, cell-line identities) for replication.

## Official-submission checklist

- Search the live site for "Nature Immunology author guidelines" and follow the current Springer Nature version.
- Re-check article-type and length/figure limits; confirm current Abstract format (unstructured, character-limited).
- Re-check data-deposition requirements for sequencing data (GEO/SRA) and flow cytometry data; confirm that accession numbers are provided before acceptance.
- Re-check the Life Sciences Reporting Summary, ARRIVE compliance, ethics/IRB approvals, and materials availability (reagent sharing expectations).
- Confirm competing-interests and funding disclosures, AI-use policy, and preprint compatibility (bioRxiv posting is generally supported).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the immunological mechanism established and why it changes the field's understanding of immune function broadly.
- [ ] The conceptual advance is legible to an immunologist working in a different sub-area — innate versus adaptive, mouse versus human.
- [ ] In vivo evidence is the backbone; in vitro data support rather than replace in vivo genetic findings.
- [ ] Multiple independent genetic alleles or rescue experiments underpin mutant-phenotype claims.
- [ ] Sequencing and flow cytometry data are deposited or ready for deposition; code is publicly available.
- [ ] The paper is framed against recent Nature Immunology and Immunity literature on this immune mechanism.

## Common desk-reject triggers

- A study that is descriptive immunophenotyping without a mechanism — "cell type X is expanded in condition Y" without explaining how or why.
- Purely in vitro or cell-line-based mechanistic findings without in vivo validation in a physiologically relevant model.
- A significant technical or methodological advance in immunological tools without a conceptual immunological discovery.
- A clinical immunology or biomarker study without mechanistic grounding in basic immune biology.
- A finding whose significance is limited to a single autoimmune disease or a single infection model without generalizable immune-biological principle.

## Re-routing decision

- Equivalent significance, arguably more molecular/cellular: `immunity` (Cell Press immunology flagship, mechanistic in vivo focus).
- Strong mechanistic immunology below the Nature Immunology significance bar but still high-quality: `science-immunology` (AAAS, broad significance valued) or `journal-of-experimental-medicine` (Rockefeller UP, in vivo rigor).
- Host-pathogen mechanism driving the immunology: `nature-microbiology` or `cell-host-and-microbe`.
- Human clinical immunology or translational immunotherapy: `science-translational-medicine` or `nature-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Immunology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the in vivo mechanistic evidence — genetic, functional, multi-approach — clear the Nature Immunology field-shifting bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / GEO-SRA deposition / Reporting Summary / ARRIVE / ethics / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
