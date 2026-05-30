---
name: energy-and-environmental-science
description: Use when targeting Energy & Environmental Science (EES, RSC) or deciding whether an energy/environment manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Energy & Environmental Science (energy-and-environmental-science)

## Journal positioning

Energy & Environmental Science (EES) is the Royal Society of Chemistry's flagship high-impact journal covering the intersection of energy science and environmental science — from solar cells and batteries to CO₂ capture and water treatment. EES expects research of broad interest to both communities: an energy paper must have clear environmental relevance, and an environmental paper must connect to energy or sustainability systems. The quantitative bar is high — real device metrics, environmental impact quantification, and techno-economic awareness are expected. The readership spans chemistry, chemical engineering, materials science, and environmental engineering. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the RSC / EES site.

## When to trigger

- The author names EES or Energy & Environmental Science as the target venue.
- An energy materials/device paper has a clear environmental co-benefit or sustainability narrative that elevates it above a pure-performance study.
- A green chemistry, CO₂ capture, or water-treatment paper is connected to energy systems and has strong quantitative results.
- The author is comparing EES, Joule, and Nature Energy and needs to understand EES's distinct scope and evidence bar.

## Scope & topic fit

- Solar energy conversion: photovoltaics, photoelectrochemical cells, solar-thermal conversion — with quantitative device performance, stability, and ideally system-level cost or environmental-impact metrics.
- Electrochemical energy storage and conversion: batteries, supercapacitors, fuel cells, electrolyzers — in practical configurations with durability and rate performance data; full-cell data strongly preferred over half-cell.
- CO₂ capture, utilization, and storage: sorbent/membrane/catalyst performance with energy penalty, selectivity, and regenerability data; lifecycle CO₂ accounting encouraged.
- Environmental remediation with energy relevance: advanced oxidation, photocatalytic water treatment, pollutant degradation — where quantitative environmental impact metrics (not just degradation efficiency) are reported.
- Hydrogen production and storage: electrolytic, thermochemical, or photochemical routes with Faradaic efficiency, energy efficiency, and durability in realistic configurations.
- Techno-economic and lifecycle analysis papers that combine energy and environmental metrics quantitatively, with transparent model assumptions and sensitivity analysis.

## Method & evidence bar

- Device performance must be quantified against the current literature: EES expects a benchmarking context, not just absolute numbers.
- Environmental impact must be quantified: a paper claiming "green" or "sustainable" must provide lifecycle assessment data, carbon-footprint calculation, or explicit comparison of energy/environmental trade-offs, not just verbal claims.
- Stability data must be collected under realistic operating conditions and over a timeframe relevant to the technology (accelerated aging acceptable if clearly specified and validated).
- Full-cell data are strongly preferred; half-cell catalyst screening is appropriate only when explicitly framed as a mechanistic study and not as a device performance advance.
- Computational papers must include experimental validation of key predictions; pure DFT screening without experimental corroboration is insufficient for EES.
- RSC journals have standard data-availability requirements; deposition of key datasets (e.g., crystallographic data via CCDC) must be completed before acceptance.

## Structure & house style

- EES publishes Papers, Communications, and Reviews; Communications are shorter with higher urgency and narrower scope; re-check current definitions on the live guide.
- The introduction must state both the energy and the environmental dimension of the problem — not just one or the other — and explain why the intersection is the key challenge.
- Abstract must be informative: results, not just intent; re-check the current word limit on the live guide.
- Figures should include: device/cell configuration schematic, performance comparison with literature (table or figure), stability data, and — where applicable — an environmental-impact panel or techno-economic cost comparison.
- Supporting Information carries full synthetic protocols, extended characterization, raw data, and model parameters.
- EES has an "Impact Statement" requirement in some submission tracks; re-check current requirements on the live guide.

## Official-submission checklist

- Search the live site for "Energy & Environmental Science author guidelines" (RSC) and follow the current version.
- Re-check article-type options (Paper vs. Communication vs. Review vs. Analysis), word/figure limits, and SI scope.
- Confirm CCDC/CIF deposition requirements for crystallographic data and any other mandatory data deposition.
- Re-check the RSC data availability policy, open-data options, and any reporting-checklist requirements.
- Confirm open-access options, APC, and licensing requirements (RSC hybrid/gold OA; re-check current policy).
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] Does the paper address both energy and environmental dimensions quantitatively — not just one?
- [ ] Are device or system performance metrics benchmarked against recent EES-tier literature?
- [ ] Is stability demonstrated under conditions that are operationally meaningful for the technology?
- [ ] Is an environmental impact metric (LCA, carbon footprint, or energy penalty) included where the sustainability framing is invoked?
- [ ] Are full-cell or realistic system-level data included, or is the half-cell framing explicitly justified as a mechanistic study?
- [ ] Is the abstract fully informative (results and conclusions), within the current word limit?

## Common desk-reject triggers

- Half-cell electrocatalysis results presented as a primary device performance advance without full-cell validation or durability data.
- "Sustainable" or "green" framing without any quantitative environmental metric: no LCA, no carbon accounting, no energy penalty comparison.
- Device performance claims without benchmarking context — reporting a number without comparing it to the current literature.
- Stability testing over hours or days in ideal conditions for a technology where hundreds or thousands of hours of realistic testing is the standard.
- Pure materials characterization study with no functional/device demonstration and no connection to an energy or environmental application.
- Computational screening study without experimental validation of key predicted systems.

## Re-routing decision

- Highest-significance energy paper with systems/policy/cross-disciplinary reach → `nature-energy` (broader audience, higher selectivity).
- Cell Press sustainable energy with full-cell, systems-quantitative framing → `joule`.
- Materials advance is the dominant story without a strong environmental dimension → `advanced-materials` or `nature-materials`.
- Environmental science advance with weaker energy connection → Environmental Science & Technology (ACS) or Environmental Science & Technology Letters (ACS).
- Chemistry mechanism is the core (not device performance) → `chem` or `nature-catalysis`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Energy & Environmental Science
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper provide quantitative device performance, environmental impact metrics, realistic stability, and benchmarking against literature?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / abstract limit / CCDC deposition / OA/APC / data availability / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
