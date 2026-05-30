---
name: physical-review-x
description: Use when targeting Physical Review X (PRX) or deciding whether a physics manuscript fits this open-access, high-impact, cross-subfield, longer-form APS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review X (physical-review-x)

## Journal positioning

Physical Review X is APS's fully open-access flagship for physics results that rank among the most significant advances in the field but require more space than the Letter format allows. PRX publishes longer articles across all of physics, with an editorial bar calibrated to cross-subfield importance: referees are asked not only whether the work is correct but whether it will be read and cited widely beyond the author's home subfield. PRX sits above the archival Physical Review family (PRB, PRD, PRC, PRE) in selectivity and alongside PRL in cross-subfield ambition, but without PRL's strict length constraint. Open-access publication under a Creative Commons license is mandatory.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the APS site and the PRX submission system.

## When to trigger

- The author has a high-significance physics result that exceeds PRL's length limit but would be arbitrarily truncated by fitting it into a Letter.
- A paper spans subfields (e.g., condensed matter + quantum information, or AMO + quantum computing) and cross-subfield importance is articulable.
- An author is deciding between PRX and `physical-review-letters`, `nature-physics`, or the subfield PRs, and needs to map significance level and length requirements.
- The open-access requirement is a factor and the author needs to understand PRX's licensing model before committing.

## Scope & topic fit

- Major advances across all APS-covered physics subfields: condensed matter, quantum information, atomic/molecular/optical, high-energy particle physics, nuclear, astrophysics/cosmology, statistical/soft/biological physics — when the result reaches across subfield boundaries.
- Large-scale experimental results (quantum computing demonstrations, precision measurements, materials characterization campaigns) that require full methodological reporting not compressible into a Letter.
- Comprehensive theoretical frameworks or new formalism with demonstrated cross-subfield applicability.
- Interdisciplinary physics results where the physics content is dominant and the interdisciplinary bridge is well developed.
- Results in quantum technologies, photonics, or topological systems with implications for multiple physics communities.

## Method & evidence bar

- PRX applies explicit cross-subfield-significance refereeing: referees from outside the author's primary specialty evaluate whether the result matters to their community.
- Experimental results require complete systematic-uncertainty reporting, reproducibility documentation, and, increasingly, data availability; large datasets should be deposited.
- Theoretical papers must present complete derivations or clearly scoped proofs; PRX does not accept work where critical steps are deferred to future papers.
- Computational physics papers need full numerical methodology, convergence analysis, and accessible code where feasible.
- The significance bar is above the archival Physical Review subfield journals but the evaluation criterion is cross-subfield impact rather than single-minded brevity (as in PRL).

## Structure & house style

- No strict length limit analogous to PRL, but manuscripts should not be padded; PRX articles are typically substantial because the result merits it, not for completeness theatre.
- The introduction must motivate the cross-subfield importance without assuming deep subfield familiarity; opening paragraphs address the board of physicists, not the specialist community.
- Supplemental Material is permitted but main-text completeness is expected; the key physics must be derivable from the article itself.
- Display items should be publication-quality and interpretable to non-specialists; schematic diagrams explaining the physical setup or concept are encouraged.
- Open-access mandatory: all articles published under a Creative Commons license; re-check current licensing options and APC waiver/funder-deal policies.

## Official-submission checklist

- Search the live site for "Physical Review X author guidelines" and follow the current APS version.
- Re-check the current APC amount and any institutional open-access agreements or APS waiver programs; open-access is non-optional.
- Re-check article-type eligibility (PRX does not publish Letters; full articles only), abstract format, and figure resolution requirements.
- Re-check APS data, code, and software availability policies; PRX has been progressively tightening these requirements.
- Confirm the cover letter explains cross-subfield significance explicitly; PRX editors use this to calibrate referee selection across divisions.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The result's significance can be articulated to a physicist from two different APS divisions not the author's own.
- [ ] The manuscript is longer than PRL allows because the physics requires it, not because supplementary detail was moved into the main text.
- [ ] All uncertainties, systematic effects, and numerical convergence checks are reported in the main text.
- [ ] Open-access APC and licensing are arranged or a waiver/institutional deal is confirmed.
- [ ] The introduction does not presuppose subfield specialist knowledge.

## Common desk-reject triggers

- A result that is correct and significant but of interest primarily within a single APS subfield community — editors redirect these to `physical-review-b`, `physical-review-d`, or peers without review.
- A manuscript structured as a Letter padded to article length without the physics requiring the expanded treatment.
- Failure to address the open-access/APC requirement before submission; PRX does not offer a hybrid option.
- An introduction written at subfield depth that cannot be followed by the PRX cross-subfield editorial board.
- Preliminary or partial results with a promised companion paper; PRX requires self-contained completeness.

## Re-routing decision

If cross-subfield significance cannot be argued: condensed matter / materials → `physical-review-b`; particles / gravitation → `physical-review-d`; quantum information (important but subfield-focused) → `prx-quantum`. If the result is Letter-length and cross-subfield important → `physical-review-letters`. If a broad non-specialist narrative can be written for a general physics audience → `nature-physics`. For quantum-technology results specifically, `prx-quantum` (also OA, APS) is a peer venue that may better serve a focused quantum-information community.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review X
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result clear PRX's cross-subfield significance + methodological completeness bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <open-access/APC / data policy / article type / cover-letter significance argument>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
