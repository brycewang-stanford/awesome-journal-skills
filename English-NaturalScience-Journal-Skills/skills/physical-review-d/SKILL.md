---
name: physical-review-d
description: Use when targeting Physical Review D (PRD) or deciding whether a particles, fields, gravitation, or cosmology manuscript fits this APS archival venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review D (physical-review-d)

## Journal positioning

Physical Review D is the APS archival journal of record for high-energy physics, particle astrophysics, gravitation, and cosmology. It covers the theoretical and experimental physics of particles and fields, general relativity, gravitational waves, dark matter and dark energy, early-universe cosmology, astroparticle physics, and the computational/lattice methods serving these communities. PRD is a high-volume, rigorous, archival venue — the physics record for the field rather than a selective highlights journal. A paper does not need to be immediately broadly significant to appear in PRD; it must be correct, complete, and a substantive contribution within its subfield. The peer community of particle physicists, relativists, and cosmologists are the primary readers and referees.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the APS site and the Physical Review D submission system.

## When to trigger

- The author is targeting PRD for a high-energy physics, gravitation, or cosmology manuscript.
- A result is being considered for both PRD and `physical-review-letters` and the author needs to determine whether it meets PRL's broad-importance bar or belongs in PRD's archival track.
- A theoretical particle-physics or GR/cosmology paper is being positioned within the APS Physical Review family.
- The author needs to understand PRD's scope boundaries versus Physical Review C (nuclear), Physical Review B (condensed), or Nature-family journals.

## Scope & topic fit

- Elementary particle physics: phenomenology, BSM models, Standard Model precision calculations (perturbative QCD, electroweak), collider physics and detector simulations, effective field theories.
- Quantum field theory: formal developments with direct application to particle physics or gravity; renormalization, path integrals, scattering amplitudes.
- General relativity and gravitation: classical GR, black-hole physics, gravitational waves (detection, waveform modelling, parameter estimation), tests of gravity.
- Cosmology: inflation, CMB physics, large-scale structure, dark matter/dark energy theory and phenomenology, primordial nucleosynthesis, gravitational lensing.
- Astroparticle physics: cosmic rays, neutrino physics and astrophysics, dark matter direct and indirect detection, multi-messenger astrophysics.
- Lattice field theory and computational hadronic physics.

## Method & evidence bar

- PRD is an archival journal; the bar is substantive correctness and contribution within the subfield, not cross-subfield broad importance. A technically sound paper that advances the subfield belongs here even without broader physics impact.
- Theoretical papers require complete derivations and clear specification of approximations; results presented without derivation require a referenced companion paper where the derivation appears.
- Phenomenological papers must specify the model assumptions and the observational/experimental inputs; conclusions must be clearly bounded by those assumptions.
- Experimental and observational papers (collider, gravitational-wave, astroparticle) require full statistical analysis, systematic-uncertainty accounting, and description of the analysis pipeline.
- Data availability, analysis code, and simulation frameworks are increasingly expected to be documented and shared; re-check current APS policies.

## Structure & house style

- PRD publishes both Letters (short, urgent results calling for rapid attention) and full Articles; article type should be chosen at submission based on the result's nature and urgency.
- No cross-subfield framing is required — PRD introductions are written for the relevant HEP/gravity/cosmology community and can assume specialist familiarity.
- Supplemental Material or appendices carry extended calculations; full derivations that would interrupt the main narrative may be placed in appendices without truncation.
- The manuscript length should match the depth of the work; PRD does not impose a brevity premium on full Articles.
- Abstract is a single unstructured paragraph; results and main conclusions should appear in the abstract for index-able completeness.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Physical Review D author guidelines" and follow the current APS version.
- Confirm article type (Letter vs. Article) and re-check length or format differences between the two.
- Re-check APS data, code, and simulation-pipeline sharing requirements; HEP analysis code sharing expectations are evolving.
- Re-check the preprint policy; arXiv is the norm for this community and APS generally permits simultaneous arXiv posting.
- Confirm whether the result overlaps with or cites published ATLAS/CMS/LHCb/LIGO/Virgo collaboration papers; collaboration papers have specific multi-author and institutional acknowledgment requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The result is a substantive advance within its subfield of HEP, gravity, or cosmology — correct, complete, and not superseded by arXiv preprints posted during review.
- [ ] The derivation or analysis is self-contained or explicitly references where missing steps are given.
- [ ] Systematic uncertainties and model-assumption boundaries are clearly stated.
- [ ] The article type (Letter vs. Article) is appropriate for the result's nature and urgency.
- [ ] arXiv posting is coordinated with co-authors and collaboration rules if applicable.

## Common desk-reject triggers

- Results that fall clearly within the scope of Physical Review C (nuclear physics) or Physical Review B (condensed-matter) submitted to PRD without justification.
- Manuscripts that propose BSM phenomenology without engaging quantitatively with existing experimental constraints or LHC data.
- Papers presenting numerical results without any analytic control or error-convergence analysis.
- Theoretical papers with major unsubstantiated steps where only the final result is given.
- Formal QFT papers with no discernible particle-physics or gravitational-physics application or consequence.

## Re-routing decision

If the result is a letter-quality major advance with cross-subfield physics significance → `physical-review-letters`. For a high-impact result needing longer treatment and cross-community visibility → `physical-review-x`. Astrophysics observations and data-driven cosmology results may also fit `the-astrophysical-journal` (AAS) or `nature-astronomy`. Gravitational-wave results with broad physics significance and non-specialist narrative potential belong at `nature-physics` or `physical-review-letters`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review D
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the result a substantive, correct, complete contribution to HEP / gravity / cosmology?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / data/code sharing / arXiv policy / collaboration acknowledgment requirements>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
