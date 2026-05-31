---
name: cancer-discovery
description: Use when targeting Cancer Discovery (AACR) or deciding whether a cancer biology or translational oncology manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cancer Discovery (cancer-discovery)

## Journal positioning

Cancer Discovery is the flagship research journal of the American Association for Cancer Research and the leading venue for high-impact cancer biology and translational oncology. Its editorial DNA is built around discoveries that fundamentally advance understanding of cancer biology and carry immediate translational implications: driver oncogenes, tumor suppressor mechanisms, clonal evolution, drug resistance, immune evasion, and precision oncology strategies — with human cancer data (tumor genomics, patient cohorts, clinical specimens, early-phase trial results) as either primary or strong corroborating evidence. Cancer Discovery occupies the tier above Cancer Cell (which accepts rigorous mechanism without a mandatory translational claim) and below Nature/Science for cancer-specific work; it is the AACR community's highest-priority outlet before submitting to broad-science venues.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AACR / Cancer Discovery platform.

## When to trigger

- The author names Cancer Discovery or the AACR flagship as the target venue.
- A cancer biology study needs venue selection among Cancer Discovery, Cancer Cell, and Nature Medicine.
- A translational oncology paper with tumor genomics and a clinical component needs framing guidance.
- The author needs Cancer Discovery's specific desk-reject risks and a ranked alternative list before submitting.

## Scope & topic fit

- Oncogene and tumor-suppressor mechanism: discovery and mechanistic characterization of driver alterations, their signaling consequences, and therapeutic vulnerabilities — with patient tumor evidence as primary or corroborating.
- Drug resistance mechanisms in cancer: genomic, epigenomic, and phenotypic resistance to targeted therapies, immunotherapies, or chemotherapy — with clinical resistance cohort data.
- Tumor immunology and immune evasion: PD-L1/immune-checkpoint mechanism, tumor microenvironment cell biology, neoantigen biology, and cellular immunotherapy mechanism — with human tumor or trial data.
- Cancer genomics: somatic mutation landscape, mutational signatures, clonal evolution, copy-number alterations — where the biological or clinical consequence of the genomic findings is mechanistically resolved.
- Precision oncology and patient stratification: biomarker-stratified clinical trial results, tumor-agnostic molecular target validation, liquid biopsy clinical utility.
- Early-phase clinical trial results paired with mechanism of action evidence: the trial is not merely an efficacy signal but provides mechanistic understanding of the therapy.

## Method & evidence bar

- Human tumor data must feature prominently as primary evidence: patient tumor genomics (WES/WGS/RNA-seq), clinical cohort analyses, patient-derived xenografts, organoids, or early-phase clinical trial results.
- Mechanistic animal studies must use patient-derived or genetically engineered models that faithfully represent human cancer biology; syngeneic or xenograft-only studies without human tumor validation will not clear the bar for high-priority original research.
- Single-cell and spatial multi-omics studies require functional validation of key findings; purely descriptive atlases of tumor heterogeneity without mechanistic or clinical follow-through are insufficient.
- Drug sensitivity and resistance studies must include patient cohort validation (resistance at relapse, clinical biomarker correlation) alongside in vitro or in vivo mechanism data.
- Statistical rigor: pre-specified primary analyses, multiple-testing correction for genomic studies, survival analyses with appropriate censoring and competing-risks handling; raw p-values without effect sizes are insufficient.
- Reporting guideline checklists (CONSORT for trials, ARRIVE for animal studies) must be completed and uploaded; sequencing data must be deposited in dbGaP, GEO, or equivalent.

## Structure & house style

- Unstructured abstract (re-check the current length limit) that states the cancer biology question, the key mechanistic or translational finding, and the significance for cancer treatment or prevention; the abstract must be compelling to a broad oncology readership, not only specialists in one cancer type.
- The introduction frames the cancer-biology gap, not the generic "cancer is a major cause of mortality" statement; editors expect the introduction to be precise about which unresolved mechanism or translational problem the paper addresses.
- Results organized around the mechanistic or translational argument: genomic discovery → functional mechanism → human tumor or clinical validation; the narrative arc must be explicit.
- Significance statement (check current format requirements): Cancer Discovery may require a short "Significance" paragraph immediately after the abstract — this must be sharp, specific, and state the implication for cancer biology or cancer therapy, not a generic novelty claim.
- Figures typically include genomic landscapes, pathway diagrams, survival curves with risk tables, and representative tumor images with quantification; scale bars and controls are required for all histology.
- Supplementary materials should carry secondary analyses and supporting data; core mechanistic and clinical results belong in the main manuscript.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Cancer Discovery author instructions" on the AACR / Cancer Discovery platform and follow the current version.
- Re-check article-type classification (Research Article, Research Brief, Review) and confirm current length and figure limits.
- Confirm prospective clinical trial registration for any human efficacy or treatment studies; upload IRB/ethics and informed-consent documentation for all human sample studies.
- Complete and upload the applicable reporting guideline checklist (CONSORT, ARRIVE, STROBE, or equivalent).
- Verify AACR conflict-of-interest and funding disclosure requirements; confirm all industry and clinical-trial sponsor relationships are disclosed.
- Re-check sequencing and multi-omics data deposition requirements (dbGaP, GEO, EGA, or equivalent) with accession numbers in the manuscript.
- Confirm "Significance" paragraph format and current AI-use disclosure policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what cancer biology mechanism or translational advance this paper delivers and what it means for cancer treatment or prevention.
- [ ] Human tumor data (genomics, clinical specimens, patient cohort, or early-phase trial) is a central primary results component — not a supplementary validation figure.
- [ ] The "Significance" paragraph is sharp, specific, and states the implication for cancer biology or therapy — not a generic novelty claim.
- [ ] Mechanistic animal or in vitro data uses patient-derived or genetically engineered models that reflect human cancer biology; model-to-patient relevance is explicitly argued.
- [ ] Sequencing data are deposited with accession numbers included; reporting guideline checklists, ethics/consent, and COI disclosures are complete.
- [ ] The paper is clearly differentiated from Cancer Cell: Cancer Discovery requires either a higher significance bar or a more developed translational/clinical component.

## Common desk-reject triggers

- Cancer biology mechanism papers relying entirely on cell lines or syngeneic mouse models with no human tumor genomic or clinical data.
- Descriptive cancer genomics papers (mutation catalogue, expression atlas) without mechanistic follow-through or clinical utility demonstration.
- Clinical trial results without mechanistic investigation; purely efficacy-focused trials belong in `journal-of-clinical-oncology` or `the-lancet-oncology`.
- Missing or generic "Significance" paragraph — Cancer Discovery editors check this as an early triage criterion.
- Papers clearly below the significance bar for Cancer Discovery that fit `cancer-cell` or a disease-specific journal; incremental advances over recently published work in the same model system.

## Re-routing decision

- A mechanistic cancer biology paper without clinical data and without a translational claim → `cancer-cell` (Cell Press; rigorous mechanism with translational relevance, does not require a clinical trial arm).
- A translational cancer paper with a practice-changing clinical trial at ASCO-guideline scale → `journal-of-clinical-oncology` (ASCO flagship) or `the-lancet-oncology`.
- A cancer paper with very broad biological significance extending beyond oncology → `nature-medicine` or `science-translational-medicine`.
- A tumor immunology or immunotherapy mechanism paper without cancer-specific primary focus → `immunity` (Cell Press) or `nature-immunology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cancer Discovery
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the human tumor data / Significance paragraph / mechanistic model-to-patient relevance clear the Cancer Discovery bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / Significance paragraph / CONSORT + ARRIVE / trial registration / IRB / data deposition / AACR COI>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
