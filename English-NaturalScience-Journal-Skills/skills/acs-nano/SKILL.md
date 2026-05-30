---
name: acs-nano
description: Use when targeting ACS Nano or deciding whether a nanoscience / nanotechnology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# ACS Nano (acs-nano)

## Journal positioning

ACS Nano is the American Chemical Society's flagship journal for nanoscience and nanotechnology, publishing research on structures, phenomena, and applications at the 1–100 nm scale across chemistry, physics, materials science, and biology. The journal serves a broad interdisciplinary nanoscience readership and expects every paper to demonstrate both rigorous nanoscale characterization and significance that extends beyond a narrow sub-community. Incremental nanoparticle synthesis papers that merely report a new variant without conceptual or application advance are actively desk-rejected. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACS Publications site.

## When to trigger

- The author names ACS Nano as the target venue for a nanoscience or nanotechnology manuscript.
- A nano-materials or nano-device paper has broad interdisciplinary significance and the author is choosing between ACS Nano, Nature Nanotechnology, and Nano Letters.
- A manuscript requires re-framing from a materials/chemistry specialty perspective into a nanoscience-breadth narrative.
- The author needs ACS Nano's specific desk-reject heuristics and credible alternative-venue guidance.

## Scope & topic fit

- Synthesis, self-assembly, and directed organization of nanostructures (nanoparticles, nanowires, 2D materials, MOFs at the nanoscale) when a new design principle or structure-property relationship is established.
- Nanoscale characterization revealing structure or phenomena not accessible at larger scales: single-particle/single-molecule studies, in-situ/operando nanoscale imaging, atomic-resolution spectroscopy.
- Nano-enabled devices and systems: sensors, actuators, energy conversion/storage at nano scales, nanoelectronics, nanophotonics, nanomedicine — with demonstrated performance advance and plausible scalability discussion.
- Biological and biomedical nanoscience: nano-bio interfaces, targeted delivery, diagnostics — when nanoscale mechanism is central, not just "nanoparticle as carrier."
- Nanoscale theory and simulation directly informing experimental design or explaining experimentally observed nanoscale phenomena.
- 2D materials, quantum dots, and van der Waals heterostructures when the advance is in understanding or exploiting nanoscale properties.

## Method & evidence bar

- Nanoscale characterization must be rigorous and appropriate: size distributions from statistically representative TEM/SEM ensembles (not cherry-picked images); XPS, Raman, and spectroscopic data with proper controls and peak assignments; zeta-potential and DLS where relevant.
- For functional/device claims, performance must be quantified with reference to state-of-the-art benchmarks; device metrics must be measured under standardized or clearly stated conditions.
- Mechanism at the nanoscale must be supported by direct evidence; correlation between morphology and property is insufficient unless mechanism is ruled in by systematic variation.
- Biomedical claims require cytotoxicity, stability, and selectivity data meeting appropriate in-vitro or in-vivo standards; proof-of-concept without any toxicity characterization is insufficient.
- Computational studies must be validated by experimental data or make specific predictions that are tested; force-field or DFT results alone are insufficient without experimental context.
- Statistical rigor: report N, error bars (standard deviation vs. standard error clearly distinguished), and reproducibility across independent samples.

## Structure & house style

- The introduction must establish the nanoscale significance: what physical/chemical phenomenon is being exploited, why the nanoscale is essential (not just convenient), and what conceptual gap this paper fills.
- ACS Nano publishes Articles and Letters; Letters are shorter with tighter focus and higher immediacy; re-check current definitions on the live guide.
- Abstract must be informative (results and conclusions, not just intent), fitting within the current word limit on the live guide.
- Figures are the primary vehicle: include size-distribution histograms, control experiments, and performance benchmarks as main-text figures when they are load-bearing for the central claim.
- Supporting Information carries extended characterization, full synthetic protocols, and additional control experiments — but the main-text figures must stand alone for the central narrative.
- TOC graphic is required and must represent the actual advance, not a stylized nanoparticle rendering.

## Official-submission checklist

- Search the live site for "ACS Nano author guidelines" and follow the current ACS Publications version.
- Re-check article-type options (Article vs. Letter vs. Review), word/page/figure limits, and abstract word limit.
- Confirm data/code availability and any deposition requirements for crystallographic or sequence data.
- Re-check TOC graphic specifications (dimensions, resolution, format).
- Confirm reporting requirements for biological assays (cell viability standards, animal use/ethics) if applicable.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why the nanoscale is essential to the discovery — not just the platform.
- [ ] The contribution is framed as a conceptual, mechanistic, or performance advance, not as synthesis of a new nanoparticle variant.
- [ ] Size distributions, characterization data, and controls are from statistically representative samples.
- [ ] Device/functional performance is benchmarked against literature state-of-the-art under equivalent conditions.
- [ ] The TOC graphic accurately represents the scientific advance, not just a pretty nanostructure image.
- [ ] All nanoscale characterization claims are backed by direct evidence, not inferred from bulk measurements.

## Common desk-reject triggers

- Incremental nanoparticle synthesis with modest property improvement and no new mechanistic insight or conceptual advance.
- Characterization-only studies (new shape/size variant of a known nanostructure) without functional demonstration or mechanistic understanding.
- Device performance claims not benchmarked against the current literature or not measured under reproducible, standardized conditions.
- Biomedical application claims without any toxicity/biocompatibility data or in-vitro validation beyond a single cell line.
- Nanoscale claims based entirely on bulk measurements with no direct nanoscale characterization.
- Scope is too narrow for ACS Nano's breadth audience — purely a solid-state physics or purely a synthetic organic chemistry paper with a nanoparticle as a footnote.

## Re-routing decision

- Highest-impact conceptual nanoscale advance → `nature-nanotechnology` (more selective, strictly conceptual-advance bar).
- Smaller, focused nanoscience advance → Nano Letters (ACS; shorter-form, faster; niche nano result acceptable).
- Materials aspect dominant over nanoscale framing → `nature-materials` or `advanced-materials`.
- Energy application is the primary narrative → `nature-energy`, `joule`, or `energy-and-environmental-science`.
- Chemical synthesis advance is the core contribution → `chem` or `journal-of-the-american-chemical-society`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACS Nano
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the nanoscale characterization and functional advance clear the ACS Nano significance + rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / abstract limit / TOC graphic / data deposition / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
