---
name: nature-structural-and-molecular-biology
description: Use when targeting Nature Structural & Molecular Biology (NSMB) or deciding whether a structural/molecular biology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Nature Structural & Molecular Biology (nature-structural-and-molecular-biology)

## Journal positioning

Nature Structural & Molecular Biology is the Springer Nature specialist journal for research at the intersection of structure and function, covering proteins, nucleic acids, macromolecular complexes, and the mechanistic molecular biology they underpin. The journal is explicitly structure-function focused: high-resolution structural determination is expected to illuminate mechanism, conformational dynamics, or biology — not to be an end in itself. Readership spans structural biologists, biochemists, cell biologists, and biophysicists for whom atomic-level mechanism is a shared language. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Springer Nature NSMB site and submission portal.

## When to trigger

- The author names NSMB as the target venue for a structure-function or mechanistic molecular-biology study.
- A cryo-EM, X-ray crystallography, NMR, or single-molecule manuscript needs evaluation for whether its biological insight clears the NSMB bar.
- A mechanistic molecular-biology paper lacking structural data is being considered alongside NSMB and sister journals (Molecular Cell, Nature Chemical Biology).
- The author needs NSMB's high-frequency desk-reject triggers and an alternative-venue list before submitting.

## Scope & topic fit

- Atomic- or near-atomic-resolution structures of proteins, RNA, DNA, or macromolecular complexes where structure illuminates conformational mechanisms, catalytic cycles, or assembly pathways.
- Single-molecule biophysics (FRET, force spectroscopy, optical tweezers) that resolves mechanistic states or dynamics unresolvable by ensemble methods.
- Mechanistic molecular biology of transcription, translation, replication, repair, splicing, or chromatin, anchored by structural or biophysical evidence.
- Allosteric mechanisms, protein-nucleic acid recognition, and molecular machines (chaperones, AAA-ATPases, motor proteins) where structure drives mechanistic insight.
- Integration of cryo-ET, subtomogram averaging, or in-cell structural methods to resolve complex architecture in a biological context.
- Chemical biology / tool-compound studies where structural data reveals a mode of action with mechanistic consequence.

## Method & evidence bar

- Structural data must be of sufficient resolution and quality to support mechanistic claims: cryo-EM maps deposited in EMDB, coordinate models in PDB, full validation statistics (FSC, map-vs-model CC, MolProbity) expected.
- Structure alone is insufficient: functional assays, biochemical experiments, or cell-based validation must show the structural observation is mechanistically meaningful.
- Single-molecule experiments require rigorous controls, statistical analysis of state dwell times/populations, and a mechanism that emerges from the ensemble of data.
- Reproducibility and data quality standards follow Springer Nature's Life Sciences Reporting Summary; deposition in public repositories is non-negotiable.
- Negative-stain EM without near-atomic detail is generally insufficient unless combined with compelling biochemical mechanism; same for purely homology-model-driven studies.

## Structure & house style

- Articles are the primary format; Letters (shorter, faster) also exist — re-check current article-type options on the live site as format policies evolve.
- The title and abstract should foreground the biological mechanism uncovered, not the technique used; "cryo-EM structure of X" is a means, not the finding.
- A strong lead figure conveys the structural landscape and identifies the mechanistic states that the rest of the paper dissects.
- Extended Data carries essential supporting experiments; Supplementary Information holds additional technical materials, validation tables, and datasets.
- A Nature Reporting Summary (Life Sciences) is required; structural-data statistics should be presented in a standardized validation table.
- Methods must be reproducible in full; software, scripts, and structural-analysis workflows should be deposited or made available on a public platform.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Nature Structural & Molecular Biology author instructions" and follow the current Springer Nature version.
- Re-check article type and length limits (word/figure limits for Articles vs. Letters), abstract format (unstructured, character-limited), and Extended Data vs. Supplementary conventions.
- Re-check structural-data deposition requirements: EMDB entry and PDB accession codes must be provided before acceptance; raw micrographs deposition policy may apply.
- Re-check the Life Sciences Reporting Summary, data/code availability statement, materials availability and accession numbers, competing-interests and funding disclosures, and AI-use policy.
- Confirm preprint policy (NSMB generally permits bioRxiv posting) and embargo requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the biological mechanism NSMB readers will gain — not the structure obtained.
- [ ] The contribution is framed as mechanistic insight, not as "first cryo-EM structure of X" without functional context.
- [ ] Every structural claim is paired with a biochemical or cell-based functional test that is logically connected to that claim.
- [ ] Structural data validation statistics are complete; EMDB and PDB accession codes are ready or obtainable before acceptance.
- [ ] The framing positions the advance against recent mechanistic literature in this system, not just against older low-resolution structures.
- [ ] Reporting Summary and data-availability statement are prepared.

## Common desk-reject triggers

- Structure reported without mechanistic payoff: "we determined the structure and it reveals the active site" without showing the active site's functional role.
- Resolution or data quality insufficient to support atomic-level claims (poor validation metrics, under-sampled conformational states).
- Purely descriptive molecular biology paper with no structural or biophysical component — better suited to Molecular Cell or EMBO Journal.
- Incremental structure of a well-studied system with no conformational or mechanistic novelty (e.g., another inhibitor-bound pose without new mechanism).
- Insufficient breadth of significance: highly specialized structure without context for why the mechanism matters to molecular biology more broadly.

## Re-routing decision

- Mechanistic molecular biology without structural data, or where structure is peripheral: `molecular-cell` (Cell Press, broader mechanistic molecular biology) or `the-embo-journal` (mechanistic depth, EMBO Press).
- Structure-function in chemical biology / small-molecule mechanism: Nature Chemical Biology.
- Plant or microbial structural biology where the biological context dominates: `the-plant-cell` or `nature-microbiology`.
- Solid, complete structural study below the NSMB novelty bar: eLife (`elife`) or Structure (Cell Press).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Structural & Molecular Biology
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the structural + functional evidence clear the NSMB mechanism bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type/length / EMDB-PDB deposition / Reporting Summary / data-code / competing interests>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
