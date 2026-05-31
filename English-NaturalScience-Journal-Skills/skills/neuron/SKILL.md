---
name: neuron
description: Use when targeting Neuron or deciding whether a neuroscience manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Neuron (neuron)

## Journal positioning

Neuron is Cell Press's flagship neuroscience journal, spanning the full breadth of the field — from synaptic molecules and ion channels through circuit computation and systems dynamics to cognition and behavior — with the expectation that every paper delivers a conceptual advance that matters across multiple levels of neuroscience. The journal is distinctively integrative: the strongest papers link molecular or cellular mechanism to circuit function or behavior, rather than residing at only one scale. The readership is the entire neuroscience community, so papers must be both technically rigorous and broadly significant; a study with impact only in a narrow model-system subfield faces heavy triage.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Press site or submission system.

## When to trigger

- The author names Neuron as the target venue.
- A neuroscience study spanning cellular/circuit/systems levels is choosing between Neuron, Nature Neuroscience, or Cell.
- A computational or systems-neuroscience paper needs to assess whether its biological insight meets the bar beyond methodological novelty.
- The author needs Neuron's desk-reject triggers and alternative venue options.

## Scope & topic fit

- Synaptic transmission, plasticity, and circuit-level computation: mechanism from molecules to neural circuit dynamics.
- Neural circuit dissection — optogenetics, chemogenetics, in vivo electrophysiology, calcium imaging — where the circuit-to-behavior link is established, not merely implied.
- Sensory, motor, and cognitive systems studies when the computational or mechanistic principle is the advance, not a description of anatomy or response properties.
- Molecular neuroscience: neurodevelopment, glia biology, axon guidance, neuronal identity specification — when linked to circuit function or disease mechanism.
- Neurological and psychiatric disease mechanisms at the circuit or cellular level: synaptic pathology, network dysfunction, neurodegeneration mechanism — but not clinical-trial results.
- Computational and theoretical neuroscience when the model makes testable predictions validated in biological data.

## Method & evidence bar

- Multi-level integration is the distinguishing Neuron standard: a purely molecular/cellular study must be anchored to circuit or behavioral relevance; a purely behavioral study must identify the circuit or cellular substrate.
- Causal intervention expected: optogenetic or chemogenetic manipulation, genetic perturbation, or pharmacological intervention combined with behavioral or physiological readout; correlation-only circuits studies face skepticism.
- Large-scale recordings (Neuropixels, two-photon population imaging) must deliver a conceptual insight about neural computation, not only a data catalogue.
- Reproducibility across animals/subjects and across experimental conditions; sample sizes sufficient for the statistical inference claimed.
- STAR Methods required; data and code availability (analysis pipelines, custom MATLAB/Python code, raw electrophysiology data to public repositories).
- Human neuroscience (fMRI, EEG, lesion) must be carefully powered and mechanistically interpreted; large N alone is not a Neuron advance.

## Structure & house style

- STAR Methods mandatory; key resources table covering antibodies, mouse lines, viral constructs, software/analysis code.
- Declarative title stating the circuit, cell type, mechanism, or computation discovered; avoid descriptive or question titles.
- Structured abstract with highlights/in-brief box per Cell Press standard.
- Main figures should be organized as a conceptual progression: establish the behavioral or physiological phenomenon, identify the circuit/cellular basis, perturb causally, explain mechanistically.
- Graphical abstract standard; source data for all quantitative panels required.
- The introduction grounds the study in the neuroscience conceptual question — not a disease burden statistic — and closes with an explicit statement of what the paper establishes.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search "Neuron author information" on the Cell Press site and follow the current version.
- Re-check article types (Article, Short Article, Brief Communication, Resource, Review), length and figure limits, and supplemental policy.
- Confirm STAR Methods and key resources table requirements.
- Re-check animal ethics (IACUC/equivalent) and human-subjects (IRB/equivalent) approval and consent documentation.
- Verify electrophysiology and imaging raw-data deposition requirements (e.g., DANDI Archive, OSF, institutional repositories).
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Confirm preprint policy and open-access/license options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the neural circuit, cellular, or molecular mechanism established and its significance for neuroscience.
- [ ] The advance integrates at least two levels of analysis (molecular-cellular, cellular-circuit, circuit-behavior).
- [ ] Causal intervention (optogenetics, genetics, pharmacology) supports the mechanistic claim; correlation alone is not the primary evidence.
- [ ] STAR Methods, key resources table, and data/code repositories are prepared.
- [ ] The framing positions the advance against the mechanistic neuroscience literature, not disease incidence or clinical need.
- [ ] Statistical power and reproducibility across animals are explicitly justified.

## Common desk-reject triggers

- A purely descriptive anatomy or transcriptomics study that maps cell types or connectivity without establishing a functional principle.
- Circuit study that identifies a correlation between neural activity and behavior but lacks causal intervention.
- Exclusively molecular/cellular study in a neuronal context with no connection to circuit function, animal behavior, or disease mechanism.
- Clinical neuroscience or neuroimaging study without a mechanistic neural circuit or cellular anchor.
- Methods or tool paper where the advance is the technology rather than the neuroscience insight — better suited to `nature-methods` or `nature-neuroscience` technical advances.

## Re-routing decision

- Equally strong mechanism but narrower subfield scope → `nature-neuroscience` (slightly more tolerant of single-level excellence within systems or cellular neuroscience).
- Paradigm-shifting advance spanning neuroscience and a broader biological question → `cell` or `science`.
- Technically excellent circuits or imaging method as the primary advance → `nature-methods`.
- Solid mechanistic study below Neuron's significance bar → `elife`, `plos-biology`, Journal of Neuroscience, or Current Biology (`current-biology`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Neuron
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the multi-level mechanism + causal intervention clear Neuron's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / STAR Methods / animal & human ethics / data-code deposition>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
