---
name: prx-quantum
description: Use when targeting PRX Quantum or deciding whether a quantum information science or quantum technology manuscript fits this APS open-access flagship venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# PRX Quantum (prx-quantum)

## Journal positioning

PRX Quantum is APS's open-access flagship journal dedicated to quantum information science, quantum computing, quantum communication, quantum sensing, and the physics of quantum technologies. Launched as quantum information science matured into a distinct discipline, PRX Quantum publishes high-impact research — both fundamental and applied — that would define the conceptual and technological frontier of the field. Like its sibling Physical Review X, it is fully open access and applies a high significance bar, but its editorial scope is deliberately focused on the quantum information and quantum technology ecosystem rather than general physics. The readership spans physicists, computer scientists, engineers, and mathematicians working on quantum systems.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the APS site and the PRX Quantum submission system.

## When to trigger

- The author is targeting PRX Quantum for a quantum information science, quantum computing, or quantum technology manuscript.
- A manuscript sits at the boundary between PRX Quantum and `physical-review-letters`, `physical-review-x`, or `nature-physics` and the author needs to understand the significance/focus distinction.
- A quantum-hardware or quantum-algorithm result needs framing guidance for PRX Quantum's editorial culture versus a Nature-family journal.
- The author needs to understand PRX Quantum's open-access requirement and significance bar before beginning the manuscript.

## Scope & topic fit

- Quantum computing: quantum algorithms, quantum error correction and fault tolerance, quantum circuit theory, quantum complexity, and their physical implementations across platforms (superconducting, trapped ion, photonic, neutral atom, spin, topological).
- Quantum communication and cryptography: quantum key distribution, quantum repeaters, quantum networks, device-independent protocols, and their security proofs.
- Quantum sensing and metrology: quantum-enhanced precision measurements, atom interferometry, quantum clocks, magnetometry — when the quantum information aspects are primary.
- Foundational quantum physics with direct connection to quantum information: entanglement theory, quantum resource theories, measurement and decoherence, many-body quantum dynamics relevant to computing or communication.
- Quantum simulation: analog and digital quantum simulation of physical models, with results relevant to understanding quantum advantage or physical systems.
- Theoretical and experimental papers are equally welcomed; cross-platform results or architecture-agnostic theory tend to score well.

## Method & evidence bar

- The significance bar is set above the archival Physical Review subfield journals (PRA, PRB, PRD) — a result that is rigorous but incremental will be redirected to Physical Review A or the appropriate subfield journal.
- Experimental demonstrations must report relevant quantum figures of merit: gate fidelities, coherence times, error rates, entanglement fidelity — benchmarked rigorously against the current state of the art.
- Algorithmic and theoretical results must demonstrate clear advantage, tight bounds, or new conceptual insights; asymptotic claims must identify the resource model and assumptions explicitly.
- Quantum error correction and fault-tolerance results should specify the noise model and threshold conditions; claims of practical advantage must engage honestly with overhead costs.
- Data, code, and software availability are increasingly expected; re-check current APS and PRX Quantum policies for quantum circuit definitions and numerical data deposition.

## Structure & house style

- PRX Quantum publishes full articles (no strict PRL-style length limit); manuscripts should be as long as the physics requires and no longer.
- The introduction must be accessible to quantum information scientists and quantum technologists from different platform backgrounds; avoid platform-specific jargon in the opening.
- Abstract: single-paragraph, accessible to the quantum information community broadly (not only one subfield like trapped ions or superconductors); state the result and its significance plainly.
- Supplemental Material or appendices carry extended proofs, additional experimental data, and circuit diagrams; main text should be self-contained for the key results.
- Open-access mandatory: Creative Commons license; re-check current APC rates, institutional agreements, and APS waiver programs before submission.
- Display items should include clear circuit diagrams, performance benchmarking figures, and device schematics as appropriate to the platform.

## Official-submission checklist

- Search the live site for "PRX Quantum author guidelines" and follow the current APS version.
- Re-check current APC, APS institutional open-access agreements, and waiver eligibility; open-access is non-optional.
- Re-check article-type options, abstract format, and any structured abstract or significance-statement requirements.
- Re-check APS data availability and code-sharing policies for quantum circuits, simulation code, and experimental datasets.
- Confirm the cover letter articulates the significance of the result to the broad PRX Quantum community, not only the platform-specific community.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] The result advances quantum information science or quantum technology at a level that will be recognized as important across platform communities.
- [ ] The introduction and abstract are accessible to quantum information scientists working on platforms other than the one used in the paper.
- [ ] All quantum figures of merit are reported and benchmarked against current state of the art.
- [ ] Open-access APC or institutional agreement is confirmed before submission.
- [ ] Claims of quantum advantage or speedup engage explicitly with the resource model, overhead, and assumptions.

## Common desk-reject triggers

- Technically correct but incremental results (e.g., marginal gate-fidelity improvements, small-scale algorithm benchmarks on known instances) without a new conceptual contribution; these go to Physical Review A.
- Experimental papers that do not benchmark against current state of the art in the relevant figure of merit.
- Theoretical results that are mathematically complete but do not identify a concrete physical implication or experimental consequence.
- Platform-specific engineering papers (e.g., cryogenic packaging or control electronics improvements) without a quantum-physics advance.
- Missing open-access APC arrangements at the time of submission.

## Re-routing decision

If the quantum result is correct but not at PRX Quantum's significance level, Physical Review A is the natural archival home for AMO and quantum-optics foundational work; quantum computing algorithms with narrow scope also fit there. If the result has cross-subfield physics significance beyond quantum information, `physical-review-x` or `physical-review-letters` may be more appropriate. Photonic quantum implementations with broad photonics significance may fit `nature-photonics`. Results with a compelling conceptual-physics narrative for a general physics readership belong at `nature-physics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] PRX Quantum
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result advance quantum information science/technology above the archival Physical Review bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <open-access/APC / data/code policy / abstract / benchmarking / cover letter>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
