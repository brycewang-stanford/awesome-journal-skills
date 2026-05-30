---
name: joule
description: Use when targeting Joule (Cell Press) or deciding whether a sustainable-energy manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Joule (joule)

## Journal positioning

Joule is the Cell Press flagship for sustainable energy research, positioned at the interface of fundamental science and real-world energy application. It publishes work that advances the science and technology of sustainable energy generation, storage, and use — but with a hard insistence on quantitative, systems-aware contextualization: results must be evaluated against real-world metrics, full device configurations (not half-cells), and techno-economic or lifecycle considerations where relevant. Joule's editorial culture is skeptical of incremental device records that lack mechanistic insight, and hostile to claims of "practical" relevance that omit stability, scalability, or cost analysis. The readership spans materials scientists, chemists, engineers, and energy-systems analysts. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press / Joule site.

## When to trigger

- The author names Joule as the target venue for a sustainable energy research manuscript.
- A manuscript has strong device performance but needs to assess whether it meets Joule's systems-aware, full-cell, real-world-metrics standard.
- The author is choosing between Joule, Nature Energy, and Energy & Environmental Science and needs to understand how the journals differ in emphasis and scope.
- The author needs Joule's specific desk-reject heuristics before submitting a photovoltaics, battery, fuel cell, or electrolysis paper.

## Scope & topic fit

- Photovoltaics: silicon, perovskite, organic, tandem, or multi-junction solar cells — when efficiency, stability, or scalability advances are accompanied by mechanistic understanding and module-level or outdoor performance data.
- Electrochemical energy storage: lithium-ion and next-generation batteries, sodium-ion, solid-state, redox-flow — full-cell performance under practical loading conditions with cycle life and rate capability data.
- Electrolysis and fuel cells: water splitting, CO₂ reduction, nitrogen reduction — in full-cell configurations, at relevant current densities and cell voltages, with Faradaic efficiency and durability data under operating conditions.
- Thermoelectrics, thermal energy storage, mechanical energy harvesting — when real-device performance metrics are central and systems-level contextualization is provided.
- Techno-economic analysis, lifecycle assessment, and energy-systems modeling when quantitative, scenario-robust, and tied directly to the journal's sustainable-energy scope.
- Perspective and Review articles synthesizing a field's direction with critical evaluation of competing approaches and quantitative benchmarking — these are a significant fraction of Joule's content.

## Method & evidence bar

- Full-cell requirement: half-cell electrocatalysis data (LSV curves, overpotentials) alone are insufficient; Joule requires demonstration in a full electrolyzer or fuel-cell configuration at relevant current densities and with durability testing.
- Stability is non-negotiable: short-term stability (hours, not days/weeks) under ideal conditions does not constitute a "stable" claim; testing must reflect realistic operating conditions (temperature, humidity, electrolyte cycling).
- Area matters: small-area device results (sub-cm²) presented without any discussion of scalability or without larger-area validation are flagged; Joule expects evidence that the result is not an artifact of miniaturization.
- Techno-economic and lifecycle papers must use current, publicly documented cost and performance assumptions; sensitivity analysis across optimistic/central/pessimistic scenarios is required.
- Record claims must be independently verifiable: certified efficiency measurements from accredited labs are expected for top-tier efficiency claims.
- Mechanism must underpin the performance advance: structure-property-function connections supported by operando or post-mortem characterization are required, not just before/after performance comparison.

## Structure & house style

- Joule follows the Cell Press format: main text, STAR Methods, and Supplementary Information; the STAR Methods section is the primary location for detailed protocols.
- The introduction must state the energy problem, quantify the gap, identify the mechanistic or systems-level insight this paper contributes, and distinguish it from recent high-profile literature — not a generic background survey.
- Device performance data must be presented with certified measurements (or clearly labeled as uncertified with appropriate caveats), full J-V or polarization curves, and EQE/stability plots as appropriate.
- Figures: include a performance-benchmarking panel that places the result in the context of current best values in the literature; readers should immediately see where this result stands.
- The Discussion must address scalability, cost trajectory, and remaining barriers to deployment — Cell Press/Joule expects authors to engage honestly with the gap between lab results and practical application.
- Graphical abstract is mandatory and must convey the system (not just a molecule) and the performance advance.

## Official-submission checklist

- Search the live site for "Joule author instructions" or "Cell Press submission guidelines" and follow the current version.
- Re-check article-type options (Article, Report, Perspective, Review, Correspondence), word/figure limits, STAR Methods requirements, and SI scope.
- Re-check graphical abstract specifications and "In Brief"/"Highlights" word limits.
- Confirm data and code availability requirements; deposition of raw device characterization data may be required.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- For efficiency record claims, re-check Joule's certification and independent verification requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] Are full-cell (not half-cell) performance data under realistic conditions the basis for the central claim?
- [ ] Is stability demonstrated over a timeframe and under conditions that are operationally relevant, not just proof-of-concept?
- [ ] Is the mechanism connecting structure/composition to performance established by direct characterization, not inferred from performance alone?
- [ ] Does a benchmarking panel show where this result stands relative to current literature?
- [ ] Does the Discussion explicitly address scalability, cost, and remaining barriers — not just claim future promise?
- [ ] Are STAR Methods, graphical abstract, and supplementary data complete and self-consistent?

## Common desk-reject triggers

- Half-cell electrocatalysis results (overpotential/TOF) presented as the primary advance with no full-cell demonstration or durability data under operating conditions.
- Small-area device efficiency record with no discussion of reproducibility across batches, no larger-area validation, and no stability data beyond short-term testing.
- Stability claim based on hours of testing under mild conditions in a field where thousands of hours of outdoor or accelerated testing is the standard.
- Techno-economic analysis using optimistic, undocumented cost assumptions with no sensitivity analysis.
- Mechanism described only by before/after performance comparison, without operando, spectroscopic, or structural evidence.
- A paper framed as "solving" a practical energy problem when the gap between the lab demonstration and real-world deployment is not acknowledged or quantified.

## Re-routing decision

- Systems-level or policy/economic framing with broader (non-materials) significance → `nature-energy` (broader cross-disciplinary readership).
- Energy materials advance where device demonstration is secondary → `nature-materials` or `advanced-materials`.
- Environmental co-benefit or environmental impact is the primary framing → `energy-and-environmental-science` or `nature-sustainability`.
- Chemistry mechanism (e.g., catalytic cycle) is the central advance, application secondary → `chem` or `nature-catalysis`.
- Nanoscale mechanism is the core contribution → `acs-nano` or `nature-nanotechnology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Joule (Cell Press)
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper provide full-cell performance, realistic stability, mechanistic evidence, and systems-level contextualization?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / STAR Methods / graphical abstract / certification / data deposition / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
