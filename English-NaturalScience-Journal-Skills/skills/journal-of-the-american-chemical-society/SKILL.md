---
name: journal-of-the-american-chemical-society
description: Use when targeting Journal of the American Chemical Society (JACS) or deciding whether a chemistry manuscript fits this ACS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of the American Chemical Society (journal-of-the-american-chemical-society)

## Journal positioning

Journal of the American Chemical Society is the flagship journal of the American Chemical Society and one of the most broadly read and cited venues in chemistry, covering the full disciplinary spectrum: organic, inorganic, physical, biological, materials, and computational chemistry. JACS demands that a paper be both scientifically significant and of general interest to the broad chemistry community — not just to specialists in the sub-field. Two article types coexist: Communications (short, urgent, conceptually distinct) and Articles (full, comprehensive, mechanistically complete); framing and length expectations differ sharply between them.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ACS submission system.

## When to trigger

- The author names JACS as the target venue.
- A chemistry manuscript has clear broad-community interest and the author is choosing between JACS, `angewandte-chemie-international-edition`, and `nature-chemistry`.
- A Communication needs framing that demonstrates both novelty and relevance beyond the originating sub-field.
- The author needs JACS's desk-reject risks and credible alternatives.

## Scope & topic fit

- Organic synthesis: new reactions, catalytic methods, total synthesis where the strategy or enabling chemistry is genuinely new.
- Inorganic and organometallic chemistry: new compound classes, bonding concepts, reactivity, or catalytic cycles with mechanistic insight.
- Physical and theoretical chemistry: new spectroscopic/analytical methods, computational frameworks, or quantitative structure-property relationships with experimental validation.
- Biological and bioorganic chemistry: chemical tools for biology, mechanistic enzymology, chemical biology probes, nucleic acid chemistry.
- Materials and supramolecular chemistry when the advance is grounded in molecular-level understanding and mechanism.

## Method & evidence bar

- For Communications: the result must be complete enough to support the central claim, not preliminary; mechanistic support is expected, not just observation of an effect.
- For Articles: comprehensive experimental scope, full mechanistic elucidation, and comparative studies that establish generality.
- Reproducibility: synthetic procedures, characterisation data (NMR, X-ray, HRMS, etc.), and yields must be sufficient for an independent laboratory to reproduce.
- Computational chemistry must be benchmarked and the level of theory justified; calculations that contradict experiment require reconciliation.
- Statistical analyses of catalytic or biological data should include error analysis; n-of-1 measurements for key claims are insufficient.

## Structure & house style

- Communications lead with a short Introduction situating the conceptual novelty; Results/Discussion and a brief Conclusions follow; SI carries detailed experimental.
- Articles have a full Introduction that positions the work against the JACS/Angew literature; Results and Discussion may be combined; SI carries full characterisation data.
- Abstracts are unstructured; the first two sentences must state the problem and the advance for a broad chemistry audience.
- A graphical abstract (TOC graphic) is required; it must be clear and self-explanatory.
- JACS uses ACS style references; Supporting Information carries full experimental, spectra, X-ray data, and computational details.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "JACS information for authors" and follow the current ACS version.
- Re-check the article type (Communication vs. Article), current length limits for main text and SI, and abstract character limit.
- Confirm TOC graphic specifications (size, format, content requirements).
- Verify data/code availability policy, X-ray crystallographic data deposition (CCDC), and any spectral data archiving requirements.
- Check ACS open-access options, licensing, conflict-of-interest, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why the broad chemistry community (not just specialists) should care about this result.
- [ ] The contribution is framed as a new concept, mechanism, or reaction principle — not as "we synthesised X for the first time."
- [ ] For Communications: mechanistic support is present and key claims are supported by multiple independent experiments.
- [ ] All compounds are fully characterised and spectra/crystallographic data are included in SI.
- [ ] TOC graphic is complete, uncluttered, and accurately represents the main finding.

## Common desk-reject triggers

- A result of high interest only within a narrow sub-field, without a clear argument for broad chemistry relevance.
- A Communication where key claims rest on a single experiment or where mechanistic assertions are speculative without supporting data.
- Missing characterisation data for new compounds; incomplete or absent NMR/HRMS in SI.
- A paper that is primarily a biological assay result or a materials performance screen with no molecular-level chemical insight.
- Submissions framed as "we report the synthesis of X" without articulating what chemical concept or principle the work advances.

## Re-routing decision

- Equally high novelty, European-community focus, or preferred short Communication format → `angewandte-chemie-international-edition`.
- Conceptual advance intended for the broadest possible chemistry readership with a narrative framing → `nature-chemistry`.
- Catalysis-centric mechanism with field-defining significance → `nature-catalysis`.
- Nanoscience or nanostructured-materials emphasis → `acs-nano`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of the American Chemical Society
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the result demonstrate broad chemical significance and mechanistic completeness?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type Communication/Article / length / TOC graphic / SI characterisation / CCDC / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
