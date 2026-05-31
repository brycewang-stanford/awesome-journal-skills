---
name: nature-catalysis
description: Use when targeting Nature Catalysis (Nat Catal) or deciding whether a catalysis manuscript fits this Springer Nature venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Catalysis (nature-catalysis)

## Journal positioning

Nature Catalysis is a Springer Nature journal dedicated to fundamental and applied research in catalysis across all sub-disciplines — heterogeneous, homogeneous, biological, and electrochemical — with a unifying editorial emphasis on mechanistic understanding and broad significance. The journal publishes original research articles and reviews aimed at the full catalysis community plus adjacent fields; a Nature Catalysis paper must matter beyond its specific reaction or system class. The defining editorial criterion is that the catalytic advance illuminates a mechanism, introduces a genuinely new design principle, or achieves a performance milestone whose conceptual implications extend across sub-fields.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature submission portal.

## When to trigger

- The author names Nature Catalysis or Nat Catal as the target venue.
- A catalysis manuscript has mechanistic depth and broad significance, and the author is choosing between Nature Catalysis, `nature-chemistry`, `journal-of-the-american-chemical-society`, and `angewandte-chemie-international-edition`.
- A manuscript on a catalytic system claims broad mechanistic insight and the author needs to assess whether the evidence and framing match the Nature Catalysis standard.
- The author needs Nature Catalysis's desk-reject risks and alternative-venue guidance.

## Scope & topic fit

- Heterogeneous catalysis: mechanistic elucidation of surface reactions, active-site identification, structure-activity relationships at atomic resolution.
- Homogeneous and organometallic catalysis: new mechanistic paradigms, new ligand/metal cooperative modes, or enantioselective catalysis with mechanistic insight.
- Electrocatalysis and photocatalysis: mechanistic studies of energy-conversion reactions (CO2 reduction, N2 fixation, water oxidation/reduction) with spectroscopic or in situ evidence.
- Biocatalysis and enzyme engineering: mechanistic understanding of natural or engineered enzymes, and design principles transferable to synthetic catalysis.
- Catalysis-related methods: new in situ / operando characterisation techniques whose primary contribution is mechanistic insight into catalytic systems.

## Method & evidence bar

- Mechanistic evidence is the defining differentiator from other chemistry journals: kinetic analysis, isotope labelling, in situ/operando spectroscopy, DFT or ab initio mechanistic calculations, or high-resolution structural characterisation must support mechanistic claims.
- Performance claims (TON, TOF, selectivity, yield) must be placed in honest context relative to prior benchmarks; overstated performance without mechanistic insight is insufficient.
- Spectroscopic and structural characterisation of catalytic intermediates or active sites is strongly valued.
- For electrocatalysis: electrode surface area normalisation, Faradaic efficiency, stability assessment, and full electrochemical characterisation are required; benchmarking against state-of-the-art is expected.
- A Nature-family reporting summary is required; re-check the current checklist.
- Data and code availability statements are required; re-check the current policy.

## Structure & house style

- The opening paragraph must frame the catalytic challenge and state the mechanistic advance for a broad catalysis audience — not just specialists in one sub-field.
- Nature Catalysis publishes Articles (full research) and Letters (shorter, rapid communications); re-check the current article-type definitions and length limits on the live site.
- Extended Data figures carry supporting mechanistic and characterisation data; main figures tell the mechanistic story.
- A Methods section follows the main text; detailed procedures and additional characterisation belong in the SI.
- Reporting summary, data/code availability statement, author contributions, and competing-interests declaration are mandatory.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Catalysis author information" and follow the current Springer Nature version.
- Re-check the article type (Article vs. Letter), current length limits for main text and abstract, and maximum figure count.
- Confirm Extended Data policy, reporting summary checklist, and data/code/catalyst availability requirements.
- For electrocatalysis manuscripts: re-check any discipline-specific checklist the journal may require.
- Verify competing-interests, author-contribution, AI-use, and preprint/embargo policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the mechanistic insight and why it matters beyond the specific reaction or system studied.
- [ ] Mechanistic claims are supported by direct experimental evidence (kinetics, spectroscopy, labelling, structural data), not performance metrics alone.
- [ ] Performance benchmarks are honestly contextualised against recent literature; inflated comparisons will be caught in review.
- [ ] The opening paragraph frames the catalytic challenge for the full catalysis community, not just the specialist sub-field.
- [ ] Reporting summary, Extended Data figures, and data/code availability statement are complete.

## Common desk-reject triggers

- A paper reporting high catalytic performance (activity, selectivity) without mechanistic investigation — a performance screen belongs in specialist catalysis journals.
- Mechanistic proposals supported only by DFT calculations without experimental validation of intermediates or rate-determining steps.
- Electrocatalysis papers missing Faradaic efficiency, stability data, or surface-area normalisation.
- Framing as an advance within one sub-field (e.g., "best TON for X reaction") without connecting to broader mechanistic principles or design guidelines.
- Missing or inadequate reporting summary or data availability statement for a Nature-family submission.

## Re-routing decision

- Catalysis with primary conceptual chemistry advance at the molecular level → `nature-chemistry` or `journal-of-the-american-chemical-society`.
- Strong catalytic methodology paper without broad mechanistic novelty → `angewandte-chemie-international-edition` or ACS Catalysis.
- Comprehensive review of a catalysis area → `chemical-reviews` or `chemical-society-reviews`.
- Materials-emphasis (catalyst design as materials problem) → nature-materials or Advanced Materials.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Catalysis
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there direct mechanistic evidence beyond performance metrics — and does the significance span sub-fields?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / Extended Data / electrocatalysis checklist / reporting summary / data-code / disclosure>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
