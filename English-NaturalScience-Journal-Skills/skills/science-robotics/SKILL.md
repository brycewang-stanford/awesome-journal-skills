---
name: science-robotics
description: Use when targeting Science Robotics (Sci Robot) or deciding whether a robotics manuscript fits this AAAS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science Robotics (science-robotics)

## Journal positioning

Science Robotics is an AAAS journal dedicated to robotics research with demonstrated capability and broad scientific or societal significance. It occupies a position analogous to other Science-family specialty journals: the bar is not incremental technical improvement in a niche robotic system but a result that shifts what is possible or understood in robotics and is legible to scientists outside the immediate sub-field. Demonstrated performance in realistic or challenging environments — not just simulation — is a recurrent editorial requirement. The readership includes roboticists, engineers, biologists, materials scientists, and clinical researchers who engage with robotics as a tool for scientific discovery or societal benefit.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAAS / Science Robotics site and the submission system.

## When to trigger

- The author names Science Robotics or Sci Robot as the target venue.
- A robotics paper claims broad significance and demonstrated capability and the author is evaluating AAAS tier versus IEEE or Nature-family alternatives.
- A paper from an adjacent field (materials, biology, medicine) involves a robotic system with field-level significance and needs venue framing.
- The author wants to identify the most common desk-reject risks for this venue.

## Scope & topic fit

- Novel robotic systems demonstrating new locomotion, manipulation, sensing, or actuation capabilities in realistic conditions.
- Soft robotics, bioinspired robotics, and morphological computation with demonstrated mechanical capability and conceptual insight.
- Human-robot interaction and collaborative robotics with demonstrated safe, effective performance in human-scale environments.
- Medical robotics, surgical systems, and rehabilitation devices where demonstrated clinical or preclinical performance is central.
- Autonomous systems and robot intelligence (perception, planning, learning) where the robotic integration and demonstrated task performance are the primary contribution.
- Robotic exploration, environmental monitoring, or disaster response with documented field performance.

## Method & evidence bar

- Demonstrated capability is the primary bar: results must show the robot doing something genuinely new, not a slightly better version of existing capabilities; real-world or realistically constrained experiments are preferred over pure simulation.
- Physical performance claims must be quantified with appropriate metrics, repeated trials, and statistical characterization; single-run demonstrations are insufficient for central claims.
- For learning-based robotics, the training environment and sim-to-real transfer assumptions must be clearly stated; evaluation in conditions that differ from training is expected.
- Fabrication and hardware reproducibility: materials, manufacturing processes, and key parameters should be described with sufficient detail for the robotics community to assess reproducibility.
- Videos and supplementary demonstrations are expected and strongly influence editorial evaluation; production quality of videos should match the significance of the claim.
- Comparison to relevant prior robotic systems is required; the performance advance must be quantified relative to credible baselines.

## Structure & house style

- AAAS format: Research Article format with abstract, introduction, results, discussion, materials and methods; re-check current Science Robotics specific requirements.
- The abstract and introduction must establish broad significance: what barrier in robotics or in the broader science/society this work removes.
- The structured abstract (if required by current instructions) should be drafted; check current AAAS requirements for this venue.
- Video supplementary material is expected for experimental results; the editorial office reviews video evidence alongside text claims.
- Main text figures should demonstrate the system in action; schematics, performance plots, and comparison tables should be integrated logically.
- Supplementary Materials carry extended methods, fabrication protocols, additional experimental data, and video captions.

## Official-submission checklist

- Search the live AAAS site for "Science Robotics information for authors" and follow the current version.
- Re-check article type (Research Article, Review, Research Resource, Focus, Perspective), length, and figure limits.
- Prepare supplementary video(s) meeting current format and size requirements; include video captions.
- Confirm data availability statement and any requirements for hardware design files or code.
- Complete AAAS ethics, competing-interest, and author-contribution disclosures.
- Check AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what robotics capability this paper enables that was not possible before, and why it matters broadly.
- [ ] Central performance claims are supported by repeated experiments with quantified statistics, not single demonstrations.
- [ ] Physical hardware demonstrations are the primary evidence; simulation results (if any) are positioned as supporting analysis.
- [ ] Supplementary video is prepared and directly substantiates the key performance claims.
- [ ] The paper positions its advance against the most capable prior robotic systems with quantitative comparisons.
- [ ] Fabrication/hardware details are sufficient for the community to assess reproducibility.

## Common desk-reject triggers

- Incremental improvement on an existing robotic system without a novel capability or conceptual advance.
- Primary evidence from simulation alone, with no physical demonstration or compelling argument for why physical results are unnecessary.
- Performance claims not supported by repeated trials and statistical characterization.
- Missing or low-quality supplementary video for experimental claims.
- Narrow technical robotics contribution without articulated broader significance beyond the immediate sub-community.

## Re-routing decision

Robotics papers with strong ML/AI framing and broader AI significance → `nature-machine-intelligence`. Computer vision or perception methods not tightly tied to physical robotic performance → `ieee-transactions-on-pattern-analysis-and-machine-intelligence`. Excellent robotics methods work that is rigorous but narrower in significance → IEEE Transactions on Robotics or the International Journal of Robotics Research. Soft-materials or actuator advance without full robotic system integration → `nature-materials` or advanced materials venues.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science Robotics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the demonstrated physical capability and significance clear the AAAS bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / video supplementary / data-code / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
