---
name: nature-machine-intelligence
description: Use when targeting Nature Machine Intelligence (Nat Mach Intell) or deciding whether an AI, ML, or robotics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Machine Intelligence (nature-machine-intelligence)

## Journal positioning

Nature Machine Intelligence is a Springer Nature journal publishing research across machine learning, artificial intelligence, robotics, and their intersections with other sciences and society. It occupies the Nature-family tier, so the bar is not a strong ML method alone but a result with conceptual significance or real-world relevance that will interest researchers across AI and the sciences more broadly. The journal explicitly attends to societal impact, ethics, fairness, and the responsible development of AI — these are not boxes to tick but genuine editorial concerns. Papers that demonstrate a compelling application of AI to a scientific or societal problem alongside methodological rigor are a strong fit.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature site and the submission system.

## When to trigger

- The author names Nature Machine Intelligence or Nat Mach Intell as the target venue.
- An ML or AI paper has strong conceptual novelty or a major real-world application and the author is choosing between this venue and specialized venues.
- A paper applying AI to scientific discovery (biology, chemistry, physics, climate) needs framing for an interdisciplinary Nature-family audience.
- The author wants to assess whether societal/ethics dimensions are adequately addressed and what desk-reject risks exist.

## Scope & topic fit

- Novel ML/AI methods with demonstrated conceptual advance or substantial real-world significance — benchmarking on existing tasks alone is insufficient.
- AI applied to scientific discovery: protein structure, drug design, materials discovery, climate modeling, astrophysics, genomics — where AI enables a result inaccessible by prior methods.
- Robotics and autonomous systems with broad significance and demonstrated capability in challenging, realistic settings.
- Human-AI interaction, explainability, and fairness research grounded in rigorous methodology.
- Computational neuroscience and cognitive modeling at the intersection of ML and brain science.
- Analyses of societal, ethical, or policy dimensions of AI, when empirically grounded and methodologically rigorous.

## Method & evidence bar

- Novelty must be conceptual or applicative at the Nature-family significance level: a marginal gain on a leaderboard does not clear the bar; a new learning paradigm, a structurally different architecture with principled justification, or a result enabling new scientific insight does.
- Empirical claims must rest on rigorous evaluation: appropriate baselines, multiple datasets or settings, statistical testing of performance differences, ablation studies establishing the source of improvement.
- Code and data availability are strongly expected; models and datasets should be released or clearly committed to release; re-check current Nature Portfolio norms.
- Ethical considerations must be addressed substantively: training data biases, dual-use risks, fairness across demographic groups, potential for misuse — where applicable.
- For AI-in-science papers, the scientific result must be validated and the AI component should not simply serve as a black-box accelerator without interpretive insight.

## Structure & house style

- The opening must frame why this advance matters beyond the ML community — what scientific, social, or technological barrier it lifts.
- Nature-family format: concise main text (Article or Letter); Methods section at end of or after main text; Extended Data for additional experiments and supplementary information for ancillary material.
- A Nature reporting summary (for life sciences / methods-dependent work) may be required; re-check current requirements.
- Figures must be self-contained and interpretable by a non-specialist: clear captions, defined notation, illustrative architecture diagrams.
- Ethics statement and data/code availability statement are required; re-check current Nature Portfolio standards for AI disclosure.
- Competition with recent advances: the introduction must position the paper against the state of the art explicitly, not claim novelty through omission.

## Official-submission checklist

- Search the live site for "Nature Machine Intelligence author instructions" and follow the current Springer Nature version.
- Re-check article type (Article, Letter, Review, Perspective, Comment), length limits, and abstract format.
- Confirm code and model availability commitments; check for Nature Portfolio data-sharing policies.
- Prepare reporting summary if required for the study type.
- Complete ethics statement, competing-interest declaration, author-contribution statement, and AI-use disclosure (for manuscript preparation).
- Confirm preprint policy and open-access / licensing options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this AI/ML result matters to researchers beyond the immediate ML subfield.
- [ ] The contribution is stated as a conceptual advance, a new capability, or a scientific discovery enabled by AI — not as a benchmark improvement alone.
- [ ] Evaluation covers multiple baselines, settings, and ablations; statistical significance is addressed.
- [ ] Ethical considerations, dual-use risks, and fairness dimensions are substantively discussed.
- [ ] Code, models, and data are committed to open release or a clear justification is given.
- [ ] Extended Data, supplementary information, and reporting summary are prepared per current instructions.

## Common desk-reject triggers

- A strong method paper with state-of-the-art results on standard benchmarks but no conceptual novelty or broader significance beyond the ML community.
- Missing or perfunctory ethics discussion for a paper with clear societal or dual-use implications.
- No code or model release and no compelling justification for the omission.
- The AI-in-science paper delivers a better prediction but not a new scientific understanding.
- Incremental extension of an existing architecture without principled motivation or demonstrably new capability.

## Re-routing decision

Excellent ML methods papers that are rigorous and complete but narrower in scope → `journal-of-machine-learning-research` or `ieee-transactions-on-pattern-analysis-and-machine-intelligence`. Robotics-specific work with demonstrated capability → `science-robotics`. Fundamental ML theory → `journal-of-machine-learning-research`. Broad-audience conceptual AI breakthrough → consider Nature or Science.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Machine Intelligence
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the conceptual advance or real-world significance clear the Nature-family bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / code-data / ethics statement / reporting summary / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
