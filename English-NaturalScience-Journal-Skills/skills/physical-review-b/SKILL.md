---
name: physical-review-b
description: Use when targeting Physical Review B (PRB) or deciding whether a condensed matter or materials physics manuscript fits this APS archival venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review B (physical-review-b)

## Journal positioning

Physical Review B is the APS journal of record for condensed matter physics and materials physics — the highest-volume journal in the Physical Review family and the primary archival venue for the condensed-matter community worldwide. PRB covers the full breadth of the field, from strongly correlated electrons and topological phases to semiconductor physics, magnetic materials, superconductivity, nanoscale systems, and the electronic-structure and computational methods that underpin the field. Like all archival Physical Review journals, the bar is substantive, rigorous correctness and a real contribution within the subfield — not cross-subfield broad importance. The condensed-matter and materials physics communities worldwide use PRB as the primary literature of record.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the APS site and the Physical Review B submission system.

## When to trigger

- The author is targeting PRB for a condensed matter or materials physics manuscript.
- A result is being evaluated for PRB versus `physical-review-letters` (broader significance required), `physical-review-x` (high-impact OA), or `nature-physics` / `nature-materials` (Nature-family significance bar).
- The author needs to distinguish PRB's archival culture from the selective Nature-family or PRL cultures.
- A manuscript has been rejected from PRL, PRX, or a Nature journal and needs re-routing to the appropriate archival venue.

## Scope & topic fit

- Electronic structure and band theory: DFT, GW, DMFT, and correlated electron methods applied to real materials or model systems.
- Superconductivity: conventional and unconventional superconductors, theory and experiment, pair symmetry, vortex dynamics.
- Topological materials: topological insulators, semimetals, Weyl/Dirac materials, topological superconductors, edge states — both theory and spectroscopic/transport experiment.
- Strongly correlated systems: Mott insulators, heavy fermions, frustrated magnets, Kondo systems, quantum spin liquids.
- Magnetism and spintronics: exchange interactions, spin-orbit coupling, magnon physics, spin transport, multiferroics.
- Nanoscale and low-dimensional systems: 2D materials, quantum dots, quantum wires, mesoscopic transport, and surface/interface physics.
- Semiconductor physics, optical properties, lattice dynamics, and phonon-mediated interactions.

## Method & evidence bar

- PRB is archival: the bar is rigorous correctness and a substantive contribution to condensed-matter or materials physics, not cross-subfield broad importance or urgency.
- Experimental papers require full characterization: sample quality documentation, measurement uncertainty analysis, control experiments, and reproducibility checks appropriate to the measurement type.
- Theoretical and computational papers must specify the Hamiltonian, approximations, convergence criteria, and the regime of validity; results presented without complete methodological transparency are returned.
- First-principles calculations must state functional choices (XC functional, U parameters, van der Waals correction, k-point and basis-set convergence) explicitly; numerical precision must be reported.
- For topological classification or symmetry-based results, the space group, symmetry indicators, and computational tools should be documented.
- Data and code availability expectations are evolving; re-check current APS policies for computational datasets and DFT/DMFT/ED code deposition.

## Structure & house style

- PRB publishes both Letters (short, urgent results in condensed-matter or materials physics requiring rapid communication within the community) and full Articles; the author chooses based on the nature of the result.
- Introductions in PRB are written for the condensed-matter and materials physics community and may assume subfield familiarity; cross-subfield framing is not required.
- Supplemental Material carries extended derivations, additional datasets, and computational details; the main text should present the key results and physics.
- Figures must clearly present spectra, band structures, phase diagrams, or transport data with complete axis labeling, units, and error bars; community standards for condensed-matter data presentation are well established.
- Reference coverage within the condensed-matter literature must be thorough; PRB reviewers will flag missing seminal or closely related work.

## Official-submission checklist

- Search the live site for "Physical Review B author guidelines" and follow the current APS version.
- Confirm article type (Letter vs. Article) and any format differences between the two.
- Re-check APS data and code availability requirements; computational condensed-matter papers increasingly require code and input files.
- Re-check the preprint policy; arXiv posting is the norm for this community (cond-mat, supr-con, mtrl-sci sections) and APS generally supports it.
- Confirm figure and table formatting requirements and SI units conventions.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The result is a substantive, rigorous contribution to condensed matter or materials physics — correct, complete, and clearly situated in the existing PRB literature.
- [ ] All computational parameters (functional, convergence, k-mesh, U values) or experimental conditions (sample synthesis, measurement geometry, temperature range) are fully stated.
- [ ] The article type (Letter vs. Article) is appropriate; PRB Letters require urgency and a result deserving rapid community attention.
- [ ] Supplemental Material and any code/data deposition are prepared.
- [ ] arXiv posting is coordinated with co-authors.

## Common desk-reject triggers

- A condensed-matter result submitted to PRB as a Letter that lacks the urgency or compactness for Letter format; editors redirect to Article or request resubmission.
- Computational papers where key DFT parameters (functional, U, k-points) are omitted or where convergence is not demonstrated.
- Experimental papers claiming a new phase or topological property without the spectroscopic, thermodynamic, or transport evidence required to support the claim in the condensed-matter community.
- Results that are purely phenomenological curve-fitting without microscopic model or mechanism.
- Manuscripts that are outside PRB scope (particle physics → `physical-review-d`; photonics-dominant result → `nature-photonics` or `physical-review-letters`).

## Re-routing decision

If the result is Letter-quality with cross-subfield significance → `physical-review-letters`. For a cross-subfield, high-impact result needing fuller treatment → `physical-review-x`. For a conceptual materials advance with a strong structure-property narrative for a broad audience → `nature-materials`. For a broad physics narrative that non-specialists can follow → `nature-physics`. Quantum-information-focused condensed-matter results (e.g., topological qubits, many-body localization as a resource) may fit `prx-quantum`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review B
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the result a rigorous, complete contribution to condensed matter or materials physics?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / computational parameters / data/code sharing / arXiv policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
