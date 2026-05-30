---
name: angewandte-chemie-international-edition
description: Use when targeting Angewandte Chemie International Edition (Angew Chem Int Ed) or deciding whether a chemistry manuscript fits this GDCh/Wiley venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Angewandte Chemie International Edition (angewandte-chemie-international-edition)

## Journal positioning

Angewandte Chemie International Edition, published by Wiley-VCH on behalf of the German Chemical Society (GDCh), is one of the two broadest and most prestigious general chemistry journals alongside JACS, and the primary European-flagship venue for chemistry. It publishes Communications (short, high-impact), Full Papers (comprehensive mechanistic studies), and Reviews/Minireviews across the full scope of chemistry. The novelty bar for Communications is high: the result must represent a genuine conceptual or practical advance, not merely a new example within an established class. Reviews are largely invited but unsolicited minireviews with a clear thesis are considered.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Wiley submission portal.

## When to trigger

- The author names Angewandte Chemie, Angew Chem, or ACIE as the target venue.
- A chemistry manuscript has high novelty and broad-community relevance and the author is choosing between Angew Chem Int Ed, `journal-of-the-american-chemical-society`, and `nature-chemistry`.
- A short Communication needs evaluation against ACIE's specific novelty bar and framing conventions.
- The author needs ACIE's desk-reject risks and credible alternative-venue guidance.

## Scope & topic fit

- Synthetic chemistry: new bond-forming reactions, catalytic methodologies, total synthesis with enabling chemistry innovation.
- Physical, computational, and theoretical chemistry: new frameworks, high-level calculations with experimental validation, mechanistic elucidation.
- Inorganic and coordination chemistry: novel compound classes, unusual bonding, reactivity, and catalysis.
- Materials and nanochemistry at the molecular level: self-assembly, supramolecular architecture, functional materials with molecular insight.
- Chemical biology and medicinal chemistry when the advance is chemical in character — new probes, mechanisms, or strategies.

## Method & evidence bar

- Communications must be complete, not preliminary: the central claim must be fully supported by the experiments presented; the journal will not accept "proof of concept" without proof.
- Mechanistic claims require supporting evidence: kinetics, isotope labelling, computational modeling, or spectroscopic characterisation — not just product observation.
- Full Papers require comprehensive substrate scope, control experiments, and detailed SI with all characterisation data.
- New compounds require full spectroscopic characterisation; crystal structures are valued where obtainable.
- Computational studies must specify the level of theory, software, and benchmarking against experiment; standalone computational papers need experimental validation or direct predictive utility.

## Structure & house style

- Communications are short (re-check current page/word limit on the live site) with a tight narrative: context → gap → result → significance in the first paragraph.
- Full Papers have a conventional structure (Introduction, Results and Discussion, Conclusion) with an extensive SI.
- A structured or unstructured abstract (re-check current requirement) appears before the main text; it must be accessible to the broad chemistry readership.
- A graphical abstract or TOC entry is required; re-check current format specifications.
- Angewandte style uses a numbered reference system (not author-year); re-check the current Wiley reference format.
- Supporting Information carries full experimental procedures, spectral data, and computational details.

## Official-submission checklist

- Search the live site for "Angewandte Chemie author guidelines" and follow the current Wiley/GDCh version.
- Re-check the article type (Communication vs. Full Paper vs. Minireview vs. Review) and the current length constraints for each.
- Confirm graphical abstract/TOC specifications and any cover-art submission option.
- Verify CCDC or CSD deposition requirements for crystal structures.
- Check GDCh membership fee waiver policy, open-access/APC options, and licensing.
- Confirm competing-interests, funding, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence articulating the conceptual or practical advance that distinguishes this from the prior literature.
- [ ] The Communication is complete (not preliminary): the central claim is fully supported by the presented experiments.
- [ ] Mechanistic assertions are backed by direct experimental or high-level computational evidence, not inferred from yield or selectivity alone.
- [ ] All new compounds are fully characterised with spectral data in SI; crystal structures deposited if reported.
- [ ] The first paragraph positions the work against recent ACIE/JACS literature without assuming sub-field specialist knowledge.

## Common desk-reject triggers

- A Communication presenting a new substrate scope or a new example within an established methodology without a fresh conceptual element.
- Mechanistic claims supported only by product distribution or yield data, without kinetic, labelling, or spectroscopic evidence.
- Insufficient characterisation data: missing NMR spectra, HRMS, or crystal structure data for key new compounds.
- A Full Paper that is essentially an incremental extension of a prior JACS/ACIE Communication without the comprehensive mechanistic depth that justifies a Full Paper format.
- Abstract and introduction pitched at specialists; the broad chemistry reader cannot determine the significance from the first paragraph.

## Re-routing decision

- ACS-community focus, or where a broader organic/inorganic/biochemistry community is the primary audience → `journal-of-the-american-chemical-society`.
- Conceptual advance for the broadest possible chemistry readership requiring a narrative essay framing → `nature-chemistry`.
- Catalysis mechanism of primary significance across sub-fields → `nature-catalysis`.
- Invited comprehensive review of a mature field → `chemical-reviews` (ACS) or `chemical-society-reviews` (RSC).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Angewandte Chemie International Edition
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result clear the ACIE novelty bar with mechanistic completeness?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type Communication/Full Paper / length / graphical abstract / CCDC / APC / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
