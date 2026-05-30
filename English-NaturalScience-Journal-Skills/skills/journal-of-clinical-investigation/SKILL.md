---
name: journal-of-clinical-investigation
description: Use when targeting Journal of Clinical Investigation (JCI) or deciding whether a translational medicine manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Clinical Investigation (journal-of-clinical-investigation)

## Journal positioning

The Journal of Clinical Investigation is published by the American Society for Clinical Investigation and is the flagship venue for disease-mechanism research that bridges fundamental biology and human medicine. JCI's defining editorial DNA is mechanism-of-disease with direct human or translational relevance: papers must deliver a clear mechanistic insight into a disease process — not merely a correlation or an association — and must ground that insight in human clinical samples, genetics, imaging, or biomarkers, with animal or in vitro models providing mechanistic depth rather than serving as the primary evidence. JCI occupies a distinct tier below the broad-significance bar of Nature Medicine or Cell but above society clinical journals; its readership is physician-scientists and translational researchers across all disease areas.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ASCI / JCI platform.

## When to trigger

- The author names JCI or the ASCI as the target venue for a disease-mechanism or translational manuscript.
- A mechanistic study of a disease process needs venue selection between JCI, Science Translational Medicine, and Nature Medicine.
- A paper with strong human-data primary evidence and mechanistic animal or in vitro support needs framing guidance.
- The author needs JCI's specific desk-reject risks and a ranked alternative-venue list before submitting.

## Scope & topic fit

- Disease mechanism studies across all organ systems and disease areas — cardiovascular, metabolic, oncologic, immunologic, infectious, neurologic — where the mechanistic insight is novel, rigorous, and grounded in human biology.
- Translational immunology, inflammation, and autoimmunity with patient-derived cells, genetic evidence, or tissue as the primary evidence layer.
- Metabolism and endocrinology disease mechanisms: insulin resistance, adipose biology, hepatic metabolism, energy homeostasis — with human cohort or genetic validation.
- Cancer biology at the level of mechanism-of-disease (driver pathway, tumor microenvironment, drug resistance mechanism) with human tumor samples or patient-derived models providing primary evidence.
- Genetic and genomic disease mechanisms: rare disease gene function, GWAS-to-mechanism follow-up, somatic mutation consequence — where mechanistic insight is the deliverable, not just variant discovery.
- Stem cell and regenerative medicine when mechanistic insight into disease or repair is primary; not methods development per se.

## Method & evidence bar

- Human clinical samples (tissue, blood, bone marrow, biopsy), patient-derived cell lines, or organoids must constitute a primary evidentiary layer — not a supplementary validation step; animal or in vitro data provides mechanistic depth but cannot stand alone.
- Genetic evidence (GWAS loci mechanistic follow-up, rare-variant functional characterization, patient-specific iPSC models) is highly valued when it connects genomic associations to disease biology.
- Mechanistic rigor: the study should interrogate a specific molecular or cellular mechanism (pathway, interaction, functional consequence) rather than cataloguing associations or correlations; "this is associated with" is not a JCI finding; "this pathway drives X via Y mechanism" is.
- Animal models must use disease-relevant models (patient-derived xenografts, humanized mice, knock-in models), not generic healthy-animal physiology; model-to-human translation must be explicitly argued.
- Multi-omics studies (single-cell, proteomics, metabolomics) are welcome when functional validation of key findings is included; descriptive multi-omics without mechanistic follow-through will not clear the bar.
- Reporting guideline checklists (ARRIVE, CONSORT, STROBE, or equivalent) must be completed; data availability and code statements expected.

## Structure & house style

- Unstructured abstract (re-check the current length limit); the abstract must state the disease question, the mechanistic finding, and the human-relevance implication in three to four crisp sentences.
- The introduction should define the specific mechanistic gap in disease biology, not just the clinical need; JCI readers are physician-scientists who demand the biology to be precise.
- Results section must be organized around mechanistic questions, not assay types; each figure should address a logical step in the mechanistic argument.
- Discussion should connect back to human disease and explain what the mechanism implies for disease understanding, biomarker development, or therapeutic targeting — without overclaiming drug development implications.
- JCI does not use STAR Methods or extended-data frameworks; supplementary methods and additional figures carry supporting data.
- Research Articles vs. Brief Reports differ in scope and length — confirm current specifications; a brief mechanistic advance may fit the Research Letter format.

## Official-submission checklist

- Search the live site for "JCI author instructions" on the ASCI / JCI platform and follow the current version.
- Re-check article-type classification (Research Article, Research Letter, Clinical Medicine, Commentary) and confirm current length and figure limits.
- Upload ethics/IRB and patient-consent documentation for all human sample studies; IACUC documentation for animal studies.
- Complete and upload the applicable reporting guideline checklist (ARRIVE, CONSORT, STROBE, or equivalent).
- Verify ASCI conflict-of-interest and funding disclosure requirements; confirm data and code availability statement.
- Re-check sequencing or multi-omics data deposition requirements (GEO, dbGaP, Zenodo, or equivalent) with accession numbers in the manuscript.
- Confirm current AI-use disclosure policy and open-access options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the specific disease mechanism this paper establishes, and the human data that grounds it.
- [ ] The contribution is framed as a mechanistic advance — a pathway, interaction, or functional consequence — not as a discovery of correlation or a biomarker association.
- [ ] Human clinical samples or patient-derived models are central to the Results, not only in a validation figure.
- [ ] Every animal or in vitro experiment is framed as mechanistic depth for a finding established in, or corroborated by, human data.
- [ ] Reporting guideline checklists, ethics/consent, and data deposition accession numbers are ready for submission.
- [ ] The abstract states the mechanism and human relevance concisely in the final two sentences.

## Common desk-reject triggers

- Mouse or cell-line studies without human clinical samples, patient-derived models, or human genetic evidence as a primary evidentiary layer.
- Descriptive multi-omics studies (transcriptomics, proteomics) that profile a disease state without mechanistic follow-through or functional validation.
- Biomarker discovery or association studies that do not establish mechanism; correlation of protein X with disease Y without mechanistic inquiry is insufficient.
- Papers primarily presenting a new research tool or technology rather than a disease mechanism; those belong in `nature-methods` or `nature-biotechnology`.
- Clinical trials or purely clinical epidemiology studies without mechanistic investigation; those belong in `circulation`, `gastroenterology`, or similar clinical venues.

## Re-routing decision

- A translational paper with a mechanism-to-clinical-application or biomarker-to-trial arc requiring a clinical plausibility demonstration → `science-translational-medicine` (AAAS; mechanism-to-bedside with clinical validation arm).
- A disease mechanism paper with very high conceptual reach and broad significance beyond a single disease area → `nature-medicine` (Nature; broader scientific impact required).
- A cancer biology mechanism paper with translational oncology framing → `cancer-discovery` (AACR) or `cancer-cell`.
- A metabolism or metabolic disease mechanism paper without strong human clinical data → `cell-metabolism` (Cell Press; accepts mechanism-in-vivo without mandatory human data).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Clinical Investigation
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the human-sample primary layer / mechanism specificity / disease context clear the JCI bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / unstructured abstract / ARRIVE or equivalent / ethics/consent / data deposition / ASCI COI>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
