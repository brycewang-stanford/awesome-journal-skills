---
name: nature-nanotechnology
description: Use when targeting Nature Nanotechnology or deciding whether a nanotechnology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Nanotechnology (nature-nanotechnology)

## Journal positioning

Nature Nanotechnology publishes papers that represent a significant conceptual advance in nanoscience and nanotechnology — research that opens a new direction, overturns an established assumption, or demonstrates an entirely new capability at the nanoscale. It is among the most selective venues in the physical sciences; the bar is not incremental performance improvement but a result that the broad nanoscience community will recognize as a milestone. The readership spans physicists, chemists, materials scientists, and biomedical engineers who work at the nanoscale. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Nature Portfolio site.

## When to trigger

- The author names Nature Nanotechnology as the target venue for a high-significance nanoscale advance.
- A manuscript demonstrates a new physical principle, new functionality, or new nano-bio capability that reshapes how the community thinks about a problem.
- The author is choosing between Nature Nanotechnology, ACS Nano, and Nature Materials and needs to assess the significance tier required.
- The author needs Nature Nanotechnology's desk-reject heuristics and alternative routing before submitting.

## Scope & topic fit

- Nanoscale quantum phenomena: single-electron/photon control, quantum coherence, spin manipulation at the nanoscale with direct measurement and functional relevance.
- 2D materials and van der Waals heterostructures when a new physical property or device paradigm is established, not incremental device fabrication.
- Molecular machines and functional nanostructures that exhibit emergent behavior not predictable from bulk analogues.
- Nano-bio: delivery, sensing, or imaging at the single-cell or single-molecule level, where the nanoscale mechanism is indispensable and the biological or medical significance is clear.
- Nanophotonics and nanoplasmonics with new physical phenomena (beyond engineering optimization of known effects).
- DNA nanotechnology, programmable self-assembly, or structural nanotechnology when a new architectural or functional principle is demonstrated.

## Method & evidence bar

- The conceptual advance must be clearly identifiable: a paper that improves device efficiency by a factor without revealing a new principle will not clear the bar.
- Direct nanoscale characterization at the relevant length scale is mandatory; ensemble-averaged measurements that do not isolate the nanoscale mechanism are insufficient.
- For functional claims, the demonstration must be compelling and statistically supported; single-device or single-particle demonstrations require rigorous statistical treatment across multiple independently prepared samples.
- Theoretical/computational work must be directly coupled to experiment — either as the basis for a surprising experimental prediction that is verified, or as an explanation of an unexpected experimental observation.
- Reproducibility: synthesis protocols and device fabrication must be described in sufficient detail for replication; Nature's reporting summary requirements apply.
- Claims involving biomedical relevance require appropriate in-vivo or mechanistically validated in-vitro evidence — cell viability alone is insufficient for drug delivery claims.

## Structure & house style

- Nature Nanotechnology publishes Articles and Letters (re-check current type options); both are short by disciplinary standards, with a large fraction of the evidence in Extended Data and Supplementary Information.
- The main text must be written for the broad nanoscience community, not for specialists: the significance of the advance must be intelligible to a physicist unfamiliar with the specific chemical system, and vice versa.
- The introduction should state the conceptual gap in one or two paragraphs, the advance in one sentence, and reserve literature review for Supplementary Information.
- Extended Data figures carry essential controls and supporting experiments; SI carries full methods and secondary data.
- Nature's reporting summary (Methods) and data/code availability statement are required; re-check current policy for specific deposition requirements.
- A "Significance statement" or equivalent plain-language summary may be required; re-check current editorial requirements.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Nanotechnology author instructions" or "Nature Portfolio submission guidelines" and follow the current version.
- Re-check article-type definitions, word/figure limits, Extended Data limits, and Supplementary Information scope.
- Re-check the Nature reporting summary requirements (statistics, reproducibility, blinding, sample sizes, animal/human research).
- Confirm data and code availability statement requirements and any deposition obligations for atomic coordinates, sequence data, or device fabrication files.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure requirements.
- Re-check preprint policy and embargo/press-office coordination requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the conceptual advance — what does the nanoscience community now know or can now do that it could not before?
- [ ] The advance is framed as a new principle, new phenomenon, or new capability, not as an improved metric.
- [ ] The paper is written for the full nanoscience community, not for a sub-specialty audience.
- [ ] Direct nanoscale characterization supports every central claim; ensemble measurements are supplementary.
- [ ] Extended Data and reporting summary are complete; reproducibility information is in the Methods.
- [ ] Significance is genuinely at the Nature-portfolio tier, not a strong ACS Nano paper re-packaged.

## Common desk-reject triggers

- Incremental performance improvement in a known system (better efficiency, higher sensitivity) without a new mechanistic or conceptual insight.
- Nanoscale application claims without direct nanoscale mechanistic evidence — bulk characterization used to infer nanoscale behavior.
- A paper addressed to a narrow specialist audience that would be a milestone within a subfield but does not open a new direction for nanoscience broadly.
- Insufficient statistical treatment: a compelling single-device or single-particle result without multi-sample replication.
- Overstated biomedical claims: "nanoparticle for cancer treatment" without direct mechanistic in-vivo evidence at the nanoscale.
- Writing resembles an ACS Nano or Advanced Materials article (comprehensive characterization, solid work) but lacks the conceptual leap needed for Nature-portfolio tier.

## Re-routing decision

- Excellent nanoscience but below the conceptual-advance threshold for Nature Nanotechnology → `acs-nano` (broader significance window) or Nano Letters (ACS; more technical, faster).
- Materials advance where nano framing is secondary → `nature-materials` (conceptual) or `advanced-materials` (breadth).
- Chemistry-driven nanoscience with sustainability/energy framing → `chem` or `joule`.
- Nano-bio advance with clinical translational emphasis → `nature-biomedical-engineering` or `nature-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Nanotechnology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper demonstrate a new nanoscale principle or capability with direct nanoscale evidence?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / word limit / Extended Data / reporting summary / data deposition / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
