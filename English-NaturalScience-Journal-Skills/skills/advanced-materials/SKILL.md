---
name: advanced-materials
description: Use when targeting Advanced Materials (Wiley) or deciding whether a materials science manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Advanced Materials (advanced-materials)

## Journal positioning

Advanced Materials is Wiley's flagship high-impact materials journal and the highest-volume venue in its tier, publishing significant advances across the full breadth of materials science — from functional polymers and soft matter to inorganic, hybrid, 2D, and bio-inspired materials. Unlike Nature Materials, Advanced Materials rewards demonstrated performance advances and thorough materials characterization within a recognized subfield, not only cross-disciplinary conceptual leaps; the bar is significant progress within a well-established paradigm or a genuinely new materials concept at breadth. The readership is the global materials science and engineering community. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Wiley Online Library site.

## When to trigger

- The author names Advanced Materials as the target venue for a high-quality materials advance.
- A manuscript demonstrates significant performance improvement or a new materials design concept that falls below the Nature Materials conceptual threshold but above a specialty-journal scope.
- The author is choosing between Advanced Materials, Nature Materials, and specialty Wiley Advanced journals and needs tier guidance.
- The author needs Advanced Materials' desk-reject triggers and credible alternatives before submitting.

## Scope & topic fit

- Electronic and energy materials: perovskites, organic semiconductors, thermoelectrics, battery electrode materials — when the advance is a demonstrated performance record with mechanistic interpretation or a new design strategy.
- Nanomaterials and nanostructures for functional applications (photocatalysis, sensing, actuation) when thorough characterization and a clear structure-function narrative are provided.
- Soft matter, hydrogels, and bio-inspired materials with new mechanical, optical, or responsive properties and a clear design rationale.
- Flexible/wearable electronics, printed electronics, and device integration when new materials-processing insights drive the advance.
- Biomedical materials — scaffolds, drug delivery, bio-interfaces — with in-vitro or in-vivo validation and a clear materials-science contribution (not primarily a biology study).
- 2D materials and heterostructures, hybrid perovskites, MOFs/COFs when new properties are demonstrated with state-of-the-art characterization.
- Review articles are a substantial fraction of the journal's content; these are typically invited or proposed through pre-submission inquiry.

## Method & evidence bar

- Characterization must be comprehensive and state-of-the-art for the material class: XRD, TEM, XPS, spectroscopy, and relevant functional testing — not just one or two techniques.
- Performance claims must be placed in context: comparison tables or benchmarking against recent literature are expected for device metrics (PCE, conductivity, specific capacity, etc.).
- Mechanism must go beyond phenomenological correlation: control experiments, compositional variation, and ideally spectroscopic or structural evidence connecting structure to function.
- Reproducibility: multi-batch synthesis, batch-to-batch variation data, and adequate sample sizes for statistical claims are expected.
- Biomedical studies must include cytotoxicity, selectivity, and relevant in-vitro validation; animal studies require ethics approval documentation.
- Review articles must cover the field comprehensively, not just the authors' own work; a balanced, critical perspective and clear future-outlook section are required.

## Structure & house style

- Advanced Materials uses a full-paper format (Communication and Full Paper; re-check current definitions); Communications are shorter with higher immediacy; Full Papers are comprehensive.
- The introduction must clearly state the materials problem, survey the key recent literature, identify the gap, and state the advance — but can be written for a materials-science specialist audience, not required to be cross-disciplinary at the Nature level.
- A ToC figure/graphical entry is required and must clearly represent the advance.
- Figures: publication-quality resolution, self-explanatory panels with complete axis labels and units; statistical representations (box plots, error bars with explicit N) are expected for performance data.
- Supporting Information carries full synthetic protocols, additional characterization, and secondary device data.
- The framing of the advance as providing "new insight," "record performance," or "enabling new application" should be specific and substantiated — generic superlatives are editorially flagged.

## Official-submission checklist

- Search the live site for "Advanced Materials author guidelines" (Wiley Online Library) and follow the current version.
- Re-check article-type options (Communication vs. Full Paper vs. Review), word/page/figure limits, and ToC figure specs.
- Confirm open-access options, APC, and licensing (Wiley hybrid journal; re-check current OA policy).
- Re-check data/code availability, deposition requirements for crystal structures (CCDC), and any reporting-checklist obligations.
- Confirm biomedical/animal-use ethics statement requirements if applicable.
- Re-check author-contribution, competing-interests, funding, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the materials advance: what is new — a record, a design strategy, or a new concept — and why it matters for the field.
- [ ] The performance claim is benchmarked against current literature with a comparison table or explicit reference to prior best values.
- [ ] Characterization is comprehensive: structural, compositional, morphological, and functional data are all included.
- [ ] Multi-batch reproducibility is demonstrated; error bars are labeled with N and statistical method.
- [ ] ToC figure accurately and specifically represents the advance.
- [ ] The paper is not re-packaged specialty-journal work — significance and quality meet the Advanced Materials tier.

## Common desk-reject triggers

- Modest performance improvement in a well-studied system without a new design principle, new mechanistic insight, or generalizable strategy.
- Incomplete characterization: a new material reported with only one or two techniques and no functional demonstration.
- Device performance claimed without a materials-science insight — this is a device engineering paper for a specialty journal.
- Review articles that are literature summaries of the authors' own group output rather than balanced, comprehensive, critical surveys.
- Figures with missing units, unlabeled axes, or inadequate resolution; panels that are not self-explanatory.
- The advance is correct but too narrow for Advanced Materials' breadth audience — appropriate for Advanced Energy Materials, Advanced Functional Materials, or Small (all Wiley).

## Re-routing decision

- Conceptual advance requiring cross-disciplinary significance → `nature-materials` (higher selectivity, conceptual-advance bar).
- Energy-specific materials advance → Advanced Energy Materials (Wiley) or `energy-and-environmental-science`.
- Nanoscience framing is central → `acs-nano` or `nature-nanotechnology`.
- Functional materials with device application focus → Advanced Functional Materials (Wiley) or Small (Wiley).
- Sustainability/environmental materials angle → `nature-sustainability` or `energy-and-environmental-science`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Advanced Materials
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper provide comprehensive characterization, benchmarked performance, and mechanistic interpretation at the Advanced Materials tier?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / figure/word limits / ToC figure / OA/APC / data deposition / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
