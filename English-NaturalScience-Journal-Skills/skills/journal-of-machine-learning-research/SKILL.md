---
name: journal-of-machine-learning-research
description: Use when targeting Journal of Machine Learning Research (JMLR) or deciding whether a machine learning methods or theory manuscript fits this open-access venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Machine Learning Research (journal-of-machine-learning-research)

## Journal positioning

Journal of Machine Learning Research (JMLR) is the primary open-access, society-run archival journal for machine learning research, publishing since 2000 under a non-profit model with no article-processing charges. It is editorially independent, author-friendly in format, and strongly archival in culture: the expectation is rigorous methods and theory, open code, and lasting scientific contribution — not fast-paced competitive benchmarking. JMLR is read by the global ML research community as a reference for foundational methods, algorithms, and theory. It is not a conference proceedings replacement and does not reward framing calibrated to leaderboard position.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the JMLR site (jmlr.org) and the editorial submission system.

## When to trigger

- The author names JMLR as the target venue.
- An ML methods or theory paper requires the archival, no-APC, open-access format and the author is assessing fit versus TPAMI, NeurIPS journal track, or Nature Machine Intelligence.
- A paper provides a rigorous theoretical analysis, a new algorithmic framework, or a well-grounded empirical methodology for which JMLR's archival depth is appropriate.
- The author wants to understand JMLR's editorial culture and rejection profile.

## Scope & topic fit

- Machine learning algorithms: supervised, unsupervised, semi-supervised, reinforcement, and self-supervised learning methods with rigorous analysis or strong theoretical grounding.
- Statistical learning theory: generalization bounds, PAC learning, information-theoretic analyses, minimax rates.
- Optimization for machine learning: convergence analysis, stochastic optimization, second-order methods.
- Probabilistic graphical models, Bayesian methods, and approximate inference with theoretical or methodological depth.
- Kernel methods, ensemble methods, and classical ML methods — still in scope when the contribution is rigorous.
- Software and datasets track (JMLR has separate tracks): significant open-source software or benchmark datasets that serve the ML community.

## Method & evidence bar

- Rigor over novelty-signaling: a contribution must be technically correct, well-motivated, and clearly situated relative to the existing literature — the standard is a careful journal referee, not a crowd-sourced conference review.
- Theory papers must include correct, complete proofs; informal arguments or proof sketches are insufficient as the primary contribution; clearly label theorems, lemmas, and corollaries.
- Empirical papers must demonstrate the method's behavior across multiple settings, include ablations, and characterize when and why the method works; cherry-picked favorable benchmarks are a known failure mode.
- Code availability is expected and is integral to JMLR's open-science identity; the software should be usable and documented.
- Reproducibility: all hyperparameters, implementation details, and random seeds must be reported; results should be reproducible from the paper and associated code.
- JMLR has no page limits; papers should be as long as needed for completeness, and not padded.

## Structure & house style

- JMLR publishes in its own open-access format with no mandatory double-column template, but follows standard ML paper conventions; re-check current style files.
- The abstract should convey the technical problem, the approach, and the main result concisely; JMLR readers are ML specialists, so technical language is appropriate.
- A thorough related-work section is expected and valued: JMLR referees will notice omissions; the section should explain technical relationships, not just list papers.
- No length limit: use appendices and supplementary material for proofs, additional experiments, and extended derivations; but the main text should be self-contained for the central claims.
- The Software track and Datasets and Benchmarks track have their own submission formats; check current JMLR track instructions.
- References should follow JMLR style; re-check the current style guide.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Visit jmlr.org for the current submission instructions; there is no APC and no standard commercial publisher portal.
- Re-check which JMLR track is appropriate (regular, Software, Datasets & Benchmarks) and follow that track's specific requirements.
- Confirm code release: a working implementation accessible from the paper is the norm, not the exception.
- Ensure all proofs (for theory papers) are complete and correctly stated; plan for extended appendix if needed.
- Check the current JMLR policy on prior conference versions of the paper.
- Complete JMLR's author disclosure requirements (competing interests, funding).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the technical contribution: algorithm, theory result, or method — and what problem it definitively addresses.
- [ ] All theoretical claims are supported by complete, formally stated proofs (theorem + proof, not informal argument).
- [ ] Empirical evaluation covers multiple settings, baselines, and ablations; implementation details allow reproduction.
- [ ] Code is publicly available and documented; the link is included in the paper.
- [ ] Related work correctly positions the contribution relative to technically adjacent ML literature.
- [ ] If submitting a prior conference version, the extension is clearly documented and meets JMLR policy.

## Common desk-reject triggers

- Incremental improvement on a standard benchmark with no theoretical insight, algorithmic novelty, or understanding of why it works.
- Theory paper with informal proofs or proof sketches presented as the primary contribution without complete formal arguments.
- No code release and no compelling reason for the omission; reproducibility failure.
- Related work that ignores technically close prior work in the ML literature.
- A paper calibrated to conference hype cycles (incremental SOTA claim, NeurIPS/ICML framing) without the depth and completeness JMLR expects.

## Re-routing decision

Papers with computer vision emphasis and archival evaluation → `ieee-transactions-on-pattern-analysis-and-machine-intelligence`. Papers with broader AI significance or real-world application framing for a mixed audience → `nature-machine-intelligence`. Papers with robotics integration and system-level demonstration → `science-robotics`. Fast-paced new results where archival depth is not yet possible → ML conference venues.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Machine Learning Research
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the technical rigor, proof completeness, and reproducibility clear the JMLR bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <track selection / code availability / proof completeness / prior-version policy / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
