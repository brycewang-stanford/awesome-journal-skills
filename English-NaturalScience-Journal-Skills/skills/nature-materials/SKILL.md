---
name: nature-materials
description: Use when targeting Nature Materials or deciding whether a materials science manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Materials (nature-materials)

## Journal positioning

Nature Materials publishes papers that represent a conceptual advance in materials science — new understanding of structure-property-function relationships, discovery of a new class of materials, or demonstration of a new principle that will redirect how the community thinks about materials design, characterization, or application. It is not a venue for the best characterization study of a known class or for incremental performance records; the advance must be conceptual. The readership spans condensed-matter physics, chemistry, and engineering, so the significance must be legible across those communities. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site.

## When to trigger

- The author names Nature Materials as the target venue for a high-significance materials advance.
- A manuscript reveals a new structure-property relationship, new material class, or new design principle that changes how the materials community approaches a problem.
- The author is choosing between Nature Materials and Advanced Materials, Nature Physics, or Nature Chemistry and needs significance-tier guidance.
- The author needs Nature Materials' desk-reject heuristics and credible re-routing options.

## Scope & topic fit

- Structural and functional materials where a new design principle — not just a new composition — is the central contribution: phonon engineering, defect-tolerant design, symmetry-driven property emergence.
- Quantum materials: new topological phases, unconventional superconductivity, correlated-electron phenomena — when the experimental observation is unambiguous and the phenomenology is new.
- Soft matter, polymers, and biological materials when the mechanical, optical, or transport property advance reveals a generalizable design principle.
- Functional materials for energy (photovoltaics, thermoelectrics, batteries, catalysts) when the paper establishes the materials-science principle underlying performance, not just the device record.
- 2D materials and heterostructures when a new material property or interface phenomenon is being reported and understood, not just another fabrication protocol.
- Materials theory/simulation that predicts a new class of stable materials, a new phase transition, or a new design rule that is subsequently (or concurrently) verified experimentally.

## Method & evidence bar

- The structural characterization must be at the state-of-the-art level for the material class: synchrotron diffraction, cryo-EM, STEM-EELS, or equivalent — and matched to the scale of the claim.
- Mechanism must be established, not merely consistent with: ruling out alternative explanations and connecting structure directly to property through systematic compositional or structural variation.
- For device/application performance claims, the paper must isolate the materials-science contribution: what principle makes this material better, not just that it is better.
- Theory and experiment must be integrated: a pure theory paper without experimental anchor, or a pure characterization paper without mechanistic understanding, does not meet the bar.
- Reproducibility: synthesis protocols must be complete; error bars and statistical sampling across independently prepared samples are required; Nature's reporting summary applies.
- Sample quality documentation (stoichiometry, defect concentration, phase purity) must be thorough, especially for quantum/functional materials.

## Structure & house style

- Nature Materials publishes Articles and Letters (re-check current type options on the live guide); both are compact relative to disciplinary norms, relying on Extended Data for essential controls.
- The introduction must state — in language accessible to physicists, chemists, and engineers alike — what materials problem is unsolved, why it matters, and what conceptual leap this paper makes.
- The central advance should be distillable to one sentence that a materials scientist in a different sub-area can immediately appreciate.
- Extended Data carries essential supporting experiments and controls; Supplementary Information carries full protocols and secondary data.
- Nature's reporting summary, data/code availability statement, and competing-interests disclosure are all mandatory; re-check current requirements for specific deposition (e.g., crystallographic data in CCDC/ICSD).
- Figures must be designed for cross-disciplinary legibility: avoid jargon-heavy panel labels; include schematic structural diagrams alongside spectroscopic data.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Materials author instructions" and follow the current Nature Portfolio version.
- Re-check article-type definitions and word/figure/Extended Data limits.
- Re-check Nature's reporting summary requirements (statistics, reproducibility, sample sizes, blinding, animal/human research).
- Confirm data and code availability statement requirements and any deposition obligations (crystal structures, DFT input/output, device fabrication files).
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Re-check preprint and embargo policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the new materials principle — not the new material composition, but the principle that generalizes.
- [ ] The advance is conceptual: a new structure-property understanding that extends beyond the specific system studied.
- [ ] Structure is directly connected to property through controlled variation; correlation is not sufficient.
- [ ] Extended Data is complete with controls and reproducibility data; reporting summary is filled in.
- [ ] The significance is legible to a physicist, a chemist, and an engineer simultaneously.
- [ ] The paper is not a device-performance record dressed as a materials advance — the materials-science principle is the headline.

## Common desk-reject triggers

- A new record performance in a known material class without a new mechanistic understanding of why performance improved.
- A comprehensive characterization study of a new composition that does not establish a new structure-property principle.
- Pure theory/simulation without experimental validation or without predicting a testable new phenomenon.
- A paper whose significance is clear within one subfield (e.g., battery materials engineering) but does not articulate a generalizable materials-science principle.
- Insufficient characterization rigor: performance claims based on one or two samples without reproducibility demonstration or proper controls.
- The advance is a great Advanced Materials paper — thorough, significant within a specialty — but lacks the conceptual reach for Nature Materials.

## Re-routing decision

- Strong materials advance below the Nature Materials conceptual bar → `advanced-materials` (Wiley; high-volume, breadth, solid significance within specialty).
- Physics-dominant advance in quantum or electronic materials → `nature-physics` or Physical Review X.
- Chemistry-dominant advance in synthesis/function → `nature-chemistry` or `chem`.
- Energy application framing is primary → `nature-energy`, `joule`, or `energy-and-environmental-science`.
- Nanoscale is the defining length scale → `nature-nanotechnology` or `acs-nano`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Materials
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper establish a new structure-property-function principle with direct structural and mechanistic evidence?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Extended Data / reporting summary / data deposition / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
